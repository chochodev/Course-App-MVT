from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.contrib import messages

from apps.accounts.mixins import LogoutRequiredMixin, LoginRequiredMixin
from apps.accounts.forms import CustomUserCreationForm


class SignUpView(View):
    template_name = 'accounts/signup.html'

    def get(self, request, *args, **kwargs):
        form = CustomUserCreationForm()
        context = {
            'form': form,
        }
        return render(request, template_name=self.template_name, context=context)
    
    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Created account for {user.first_name}')

            return HttpResponse('Signed up user')
            # return redirect('home')
        return redirect('signup')

class SignInView(LoginView):
    template_name = 'accounts/signin.html'

    def form_valid(self, form):
        user = form.get_user()
        user.is_active = True
        user.save()
        messages.success(self.request, f'Signed In as {user.first_name}')

        return super().form_valid(form)

    def get_success_url(self):
        return redirect('signup')
        # return reverse('home')
    
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