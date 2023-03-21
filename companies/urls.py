from django.urls import path
from companies.views import CreateListCompanyView

app_name = "companies"

urlpatterns = [
    path("", view=CreateListCompanyView.as_view()),
]
