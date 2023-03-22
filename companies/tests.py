from django.test import TestCase
from django.urls import reverse
from companies.models import CompanyModel
from company_members.models import CompanyMemberModel, CompanyMemberRoles
from rest_framework.test import APIClient
from rest_framework import status
import json


class UserListTests(TestCase):
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
        url = reverse("companies:index")
        client = APIClient()

        response = client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_company_protected_with_authorization(self):
        url = reverse("companies:index")
        client = APIClient()

        response = client.post(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_gets_only_companies_they_are_members_of(self):
        url = reverse("companies:index")
        client = APIClient()

        user_companies = CompanyModel.objects.all().filter(members__user=self.test_user["id"])
        all_companies = CompanyModel.objects.all()

        client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

        response = client.get(url)
        parsed_response_content = json.loads(response.content)
        response_companies = parsed_response_content["results"]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertCountEqual(
            [company["id"] for company in response_companies], [str(company.id) for company in user_companies]
        )
        self.assertLess(len(response_companies), len(all_companies))

    def test_company_is_created_with_calling_user_as_its_admin(self):
        url = reverse("companies:index")
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
