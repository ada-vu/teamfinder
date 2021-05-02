from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["cover_letter"]