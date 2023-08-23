from django import forms
from apps.courses.models import Enroll

class EnrollForm(forms.ModelForm):
    class Meta:
        model = Enroll
        fields = ["name", "surname", "course", "email", "phone_number"]