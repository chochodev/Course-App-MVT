from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.views import View
from apps.accounts.forms import CustomUserCreationForm

# Create your views here.

class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = CustomUserCreationForm()

        context = {
            'form': form
        }
        return HttpResponse('<h2>Sign up page</h2>')
    
    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Created account for {user.first_name}')