# For OAuth
from django.contrib.auth.views import LoginView, LogoutView
from allauth.account.views import SignupView
# EndFor
from django.shortcuts import render, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.views import View
from apps.accounts.forms import CustomUserCreationForm


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

            return HttpResponse('Signed up user')
        return HttpResponse('Error while signing in')

class SignInView(LoginView):
    template_name = ''

    def form_valid(self, form):
        messages.success(self.request, 'Sign in success')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('signup')
        # return reverse('home')
    
class SignOutView(LogoutView):

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, 'Sign out success')
        return super().dispatch(request, *args, **kwargs)
    
    def get_next_page(self):
        return reverse('signin')