from django.test import TestCase
from django.urls import reverse
from companies.models import CompanyModel
from rest_framework.test import APIClient
from rest_framework import status
import json


class UserListTests(TestCase):
    fixtures = ["users_fixture.json", "companies_fixture.json", "company_members_fixture.json"]
    access_token = ""

    def setUp(self) -> None:
        auth_url = reverse("users:login")
        client = APIClient()
        response = client.post(path=auth_url, data={"email": "user@example.com", "password": "test"}, format="json")

        parsed_response_content = json.loads(response.content)

        self.access_token = parsed_response_content["access"]

    def test_get_companies_protected_with_authorization(self):
        url = reverse("companies:index")

        client = APIClient()

        response = client.get(url, HTTP_AUTHORIZATION="Bearer" + self.access_token)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_gets_only_companies_they_are_members_of(self):
        url = reverse("companies:index")

        user_companies = CompanyModel.objects.all().filter(members__user=1)
        all_companies = CompanyModel.objects.all()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

        response = client.get(url)
        parsed_response_content = json.loads(response.content)
        response_companies = parsed_response_content["results"]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertCountEqual(
            [company["id"] for company in response_companies], [str(company.id) for company in user_companies]
        )
        self.assertLess(len(response_companies), len(all_companies))
