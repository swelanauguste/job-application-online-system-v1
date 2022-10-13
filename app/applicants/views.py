from django.views.generic import CreateView, DetailView, ListView

from .forms import ApplicantCreateForm
from .models import Applicant


class ApplicantCreateView(CreateView):
    model = Applicant
    form_class = ApplicantCreateForm


class ApplicantDetailView(DetailView):
    model = Applicant


class ApplicantListView(ListView):
    model = Applicant
