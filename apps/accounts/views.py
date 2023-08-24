from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password, make_password

from apps.accounts.models import User
from apps.accounts.mixins import LogoutRequiredMixin, LoginRequiredMixin
from apps.accounts.forms import CustomUserSignUpForm, CustomUserSignInForm


class SignUpView(View):
    template_name = 'accounts/signup.html'

    def get(self, request, *args, **kwargs):
        form = CustomUserSignUpForm()
        context = {
            'form': form,
        }
        return render(request, template_name=self.template_name, context=context)
    
    def post(self, request, *args, **kwargs):
        form = CustomUserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Created account for {user.first_name}')

            return HttpResponse('Signed up user')
            # return redirect('home')
        return HttpResponse('Error during, sign up')
        # return redirect('signup')

class SignInView(View):
    template_name = 'accounts/signin.html'

    def get(self, request, *args, **kwargs):
        form = CustomUserSignInForm()
        context = {
            'form':form,
        } 
        return render(request, template_name=self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = CustomUserSignInForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request, 
                username=form.cleaned_data['username_or_email'], 
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                session = request.session['_auth_user_id']
                print('Session ID: ', session)
                return redirect('home')
            messages.error('Invalid credentials') 
        return redirect('signin')
    
class SignOutView(LogoutRequiredMixin, LogoutView):
    def get_next_page(self):
        next_page = super().get_next_page()
        if next_page:
            user = self.request.user
            user.is_active = False
            user.save()
            return next_page
        else:
            return self.request.session.get('next_page', reverse('signout'))