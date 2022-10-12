from django import forms

from .models import Applicant


class ApplicantCreateForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = "__all__"
        exclude = ("passport", "address", "contact")
        widgets = {
            'alias_name': forms.Textarea(attrs={"rows": 3}),
            'marks': forms.Textarea(attrs={"rows": 3}),
            'dob': forms.TextInput(attrs={"type": "date"}),
            # 'overstayed': forms.RadioSelect()(),
        }
