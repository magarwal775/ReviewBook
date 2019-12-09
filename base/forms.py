from django import forms
from django.contrib.auth.forms import UserCreationForm

from base.models import Account


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid Email Address.')

    class Meta:
        model = Account
        fields = ("first_name", "last_name", "username", "email", "dob", "password1", "password2")
