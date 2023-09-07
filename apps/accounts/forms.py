from django.contrib.auth.forms import UserCreationForm
from django import forms
from apps.accounts.models import User

class UserSignUpForm(UserCreationForm):
  first_name = forms.CharField(
      max_length=25,
      label='First name',
      widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder':'First Name'}),
    )
  last_name = forms.CharField(
    max_length=25,
    label='Last name',
    widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder':'Last Name'}),
  )
  email = forms.EmailField(
    label='Email',
    error_messages={
      'unique': '{value} already exist',
      'required': 'Email is required',
      'invalid': '{value} is invalid, Enter a valid address',
    },
    widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder':'Email'}),
  )
  username = forms.CharField(
    label='Username',
    error_messages={
      'unique': '{value} is already taken',
      'required': 'Username is required',
    },
    widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder':'Username'}),
  )
  password1 = forms.CharField(
    max_length=40,
    label='Password', 
    error_messages={
      'password_mismatch':'Passwords do not match',
    },
    widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder':'Password'})
  )
  password2 = forms.CharField(
    max_length=40,
    label='Confirm Password', 
    error_messages={
      'password_mismatch':'Passwords do not match',
    },
    widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder':'Confirm Password'})
  )

  def check(self):
    cleaned_data = super().clean()
    password1 = cleaned_data.get('password1')
    password2 = cleaned_data.get('password2')

    if password1 != password2:
      raise forms.ValidationError(self.fields['password2'].error_messages[{
        'password_mismatch':'Passwords do not match',
      }])
    return cleaned_data

  class Meta:
    model = User
    fields = [
        'first_name',
        'last_name',
        'email',
        'username',
        'password1',
        'password2',
    ]