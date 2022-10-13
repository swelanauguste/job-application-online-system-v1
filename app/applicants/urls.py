from django.urls import path

from . import views

app_name = "applicant"

urlpatterns = [
    path("", views.ApplicantListView.as_view(), name="applicant-list"),
    path("create/", views.ApplicantCreateView.as_view(), name="applicant-create"),
    path(
        "detail/<int:pk>/",
        views.ApplicantDetailView.as_view(),
        name="applicant-detail",
    ),
]
