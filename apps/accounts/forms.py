from django.contrib.auth.forms import UserCreationForm
from django import forms
from apps.accounts.models import User

class CustomErrorMessages:
    email = {
        "unique": "Email address already registered",
        "required": "This field is required",
        "invalid": "Enter a valid email address",
    }
    phone = {
        "unique": "Phone number already registered",
        "required": "This field is required",
    }

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=25,
        label="First name",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    last_name = forms.CharField(
        max_length=25,
        label="Last name",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    email = forms.EmailField(
        label="Email",
        error_messages=CustomErrorMessages.email,
        widget=forms.EmailInput(attrs={"class": "form-control"}),
    )
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password2 = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            # "tz",
            "password1",
            "password2",
        ]

