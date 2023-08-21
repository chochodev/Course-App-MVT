from django.contrib.auth.forms import UserCreationForm
from django import forms
from apps.accounts.models import User


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=25,
        label="First name",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"First Name"}),
    )
    last_name = forms.CharField(
        max_length=25,
        label="Last name",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Last Name"}),
    )
    email = forms.EmailField(
        label="Email",
        error_messages={
            "unique": "{value} already exist",
            "required": "Email is required",
            "invalid": "{value} is invalid, Enter a valid address",
        },
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder":"Email"}),
    )
    username = forms.CharField(
        label="Username",
        error_messages={
            "unique": "{value} is already taken",
            "required": "Username is required",
        },
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder":"Username"}),
    )
    password1 = forms.CharField(
        max_length=40,
        label="Password", 
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder":"Password"})
    )
    password2 = forms.CharField(
        max_length=40,
        label="Confirm Password", 
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder":"Confirm Password"})
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2",
        ]

