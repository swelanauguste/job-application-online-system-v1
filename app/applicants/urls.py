from django.urls import path

from . import views

app_name = "applicant"

urlpatterns = [
    path("create/", views.ApplicantCreateView.as_view(), name="application-create"),
    path(
        "detail/<int:pk>/",
        views.ApplicantDetailView.as_view(),
        name="application-detail",
    ),
]
