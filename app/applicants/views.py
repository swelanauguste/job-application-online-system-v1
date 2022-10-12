from django.views.generic import CreateView, DetailView

from .models import Applicant
from .forms import ApplicantCreateForm


class ApplicantCreateView(CreateView):
    model = Applicant
    form_class = ApplicantCreateForm


class ApplicantDetailView(DetailView):
    model = Applicant
