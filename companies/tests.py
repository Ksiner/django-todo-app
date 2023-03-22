from django.test import TestCase
from django.urls import reverse
from companies.models import CompanyModel
from company_members.models import CompanyMemberModel, CompanyMemberRoles
from rest_framework.test import APIClient
from rest_framework import status
import json


class GetAuthorizedClientMixin:
    def get_authorized_client(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

        return client


class CompanyListViewTests(TestCase, GetAuthorizedClientMixin):
    viewname = "companies:index"
    fixtures = ["users_fixture.json", "companies_fixture.json", "company_members_fixture.json"]
    access_token = ""
    test_user = dict({"id": 1, "email": "user@example.com", "password": "test"})

    def setUp(self) -> None:
        auth_url = reverse("users:login")
        client = APIClient()
        response = client.post(
            path=auth_url,
            data={"email": self.test_user["email"], "password": self.test_user["password"]},
            format="json",
        )

        parsed_response_content = json.loads(response.content)

        self.access_token = parsed_response_content["access"]

    def test_get_companies_protected_with_authorization(self):
        url = reverse(self.viewname)
        client = APIClient()

        response = client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_company_protected_with_authorization(self):
        url = reverse(self.viewname)
        client = APIClient()

        response = client.post(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_gets_only_companies_they_are_members_of(self):
        url = reverse(self.viewname)
        client = self.get_authorized_client()

        user_companies = CompanyModel.objects.all().filter(members__user=self.test_user["id"])
        all_companies = CompanyModel.objects.all()

        response = client.get(url)
        parsed_response_content = json.loads(response.content)
        response_companies = parsed_response_content["results"]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertCountEqual(
            [company["id"] for company in response_companies], [str(company.id) for company in user_companies]
        )
        self.assertLess(len(response_companies), len(all_companies))

    def test_company_is_created_with_calling_user_as_its_admin(self):
        url = reverse(self.viewname)
        client = APIClient()
        test_company_name = "test company"

        client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

        response = client.post(url, data={"name": test_company_name})
        parsed_response_data = json.loads(response.content)

        self.assertEqual(parsed_response_data["name"], test_company_name)

        target_company_member = CompanyMemberModel.objects.filter(company=parsed_response_data["id"]).first()

        self.assertIsNotNone(target_company_member)
        self.assertEqual(target_company_member.user_id, self.test_user["id"])
        self.assertEqual(target_company_member.role, CompanyMemberRoles.ADMIN.value)


class CompanyDetailsViewTests(TestCase, GetAuthorizedClientMixin):
    viewname = "companies:detail"
    fixtures = ["users_fixture.json", "companies_fixture.json", "company_members_fixture.json"]
    access_token = ""
    test_user = dict({"id": 1, "email": "user@example.com", "password": "test"})
    test_admin_user_company_id = "66ab263f-d0be-498f-9c1b-974ce17a633d"
    test_member_user_company_id = "7eff46f2-a269-4bb0-9241-9413ffa7d609"
    test_alien_company_id = "fe940a86-c25f-4ad2-957d-cf2cf090ceda"

    def setUp(self) -> None:
        auth_url = reverse("users:login")
        client = APIClient()
        response = client.post(
            path=auth_url,
            data={"email": self.test_user["email"], "password": self.test_user["password"]},
            format="json",
        )

        parsed_response_content = json.loads(response.content)

        self.access_token = parsed_response_content["access"]

    def test_get_company_protected_with_authorization(self):
        url = reverse(self.viewname, args=(self.test_admin_user_company_id,))
        client = APIClient()

        response = client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_company_protected_with_authorization(self):
        url = reverse(self.viewname, args=(self.test_admin_user_company_id,))
        client = APIClient()

        response = client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_users_can_access_only_company_they_are_members_of(self):
        client = self.get_authorized_client()

        correct_url = reverse(self.viewname, args=(self.test_admin_user_company_id,))
        correct_response = client.get(correct_url)
        parsed_correct_response_data = json.loads(correct_response.content)

        self.assertEqual(correct_response.status_code, status.HTTP_200_OK)
        self.assertEqual(parsed_correct_response_data["id"], self.test_admin_user_company_id)

        wrong_url = reverse(self.viewname, args=(self.test_alien_company_id,))

        wrong_get_response = client.get(wrong_url)
        self.assertEqual(wrong_get_response.status_code, status.HTTP_404_NOT_FOUND)

        wrong_patch_response = client.get(wrong_url)
        self.assertEqual(wrong_patch_response.status_code, status.HTTP_404_NOT_FOUND)

        wrong_put_response = client.get(wrong_url)
        self.assertEqual(wrong_put_response.status_code, status.HTTP_404_NOT_FOUND)

        wrong_delete_response = client.get(wrong_url)
        self.assertEqual(wrong_delete_response.status_code, status.HTTP_404_NOT_FOUND)

    def test_users_can_update_only_company_they_are_admins_of(self):
        client = self.get_authorized_client()

        admin_company_url = reverse(self.viewname, args=(self.test_admin_user_company_id,))
        admin_company_response = client.patch(admin_company_url, data={"name": "updated name"})
        admin_company_parsed_response = json.loads(admin_company_response.content)
        updated_company = CompanyModel.objects.filter(pk=self.test_admin_user_company_id).first()

        self.assertEqual(admin_company_response.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_company.name, "updated name")
        self.assertEqual(admin_company_parsed_response["name"], "updated name")

        member_company_url = reverse(self.viewname, args=(self.test_member_user_company_id,))
        member_company_response = client.patch(member_company_url)
        preserved_company = CompanyModel.objects.filter(pk=self.test_member_user_company_id).first()

        self.assertEqual(member_company_response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertIsNotNone(preserved_company)

    def test_users_can_delete_only_company_they_are_admins_of(self):
        client = self.get_authorized_client()

        admin_company_url = reverse(self.viewname, args=(self.test_admin_user_company_id,))
        admin_company_response = client.delete(admin_company_url)
        deleted_company = CompanyModel.objects.filter(pk=self.test_admin_user_company_id).first()

        self.assertEqual(admin_company_response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertIsNone(deleted_company)

        member_company_url = reverse(self.viewname, args=(self.test_member_user_company_id,))
        member_company_response = client.delete(member_company_url)
        preserved_company = CompanyModel.objects.filter(pk=self.test_member_user_company_id).first()

        self.assertEqual(member_company_response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertIsNotNone(preserved_company)
