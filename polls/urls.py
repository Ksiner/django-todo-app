from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path(route='', view=views.IndexView.as_view(), name='index'),
    path(route='<int:pk>/', view=views.DetailView.as_view(), name='detail'),
    path(route='<int:pk>/results/', view=views.ResultsView.as_view(), name='results'),
    path(route='<int:pk>/vote/', view=views.vote, name='vote'),
]