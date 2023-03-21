from django.urls import path
from companies.views import CreateListCompanyView, RetrieveUpdateDestroyCompanyView

app_name = "companies"

urlpatterns = [
    path("", view=CreateListCompanyView.as_view()),
    path("/<uuid:pk>", view=RetrieveUpdateDestroyCompanyView.as_view()),
]
