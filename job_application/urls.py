from django.urls import path
from .views import HomeView,ApplicantListView,SaveNotes

app_name = "job_application"

urlpatterns = [
    path("",HomeView.as_view(),name="home"),
    path("applications/list/",ApplicantListView.as_view(),name="app-list"),
    path("save-notes/<int:pk>",SaveNotes.as_view(),name="save-notes")
]