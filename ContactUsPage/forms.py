from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import re
from .models import Contactus


class UserForm(forms.ModelForm):
    class Meta:
        model = Contactus
        fields = ['Name', 'Email', 'Message']


def clean_name(self):
    name = self.cleaned_data.get('name')
    if not re.match(r'^[a-zA-Z\s]*$', name):
        raise ValidationError("Name should only contain letters and spaces")


def clean_Email(self):
    email = self.cleaned_data.get('Email')
    try:
        validate_email(email)
    except ValidationError:
        raise ValidationError("Invalid email")
    return email


def clean_Message(self):
    message = self.cleaned_data.get('Message')
    if len(message) < 10:
        raise ValidationError("Message should be at least 10 characters long")
    return message
