from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import Group
from django.db.models import Q
from apps.accounts.forms import UserSignUpForm
from apps.accounts.models import User


class SignUpView(View):
  template = 'accounts/signup.html'

  def get(self, request):
    form = UserSignUpForm()
    context = {'form':form}

    return render(request, template_name=self.template, context=context)
  
  def post(self, request):
    form = UserSignUpForm(request.POST)

    if form.is_valid():
      user = form.save()
      # Adds a user to a group / creates one if group does not exist 
      group, created = Group.objects.using('default').get_or_create(name='suscribers')
      # admin, managers, contributors, suscribers, premium suscribers
      user.groups.add(group)
      user.save()
      messages.success(request, f'Account has been created for {user.username}.')
      return redirect('home')
    else:
      # GET ERROR MESSAGES
      error_messages = form.errors.items()

      if error_messages:
        for field, errors in error_messages:
          error_message = ', '.join(errors)
      else:
        error_message = 'An error occured with your submission.'

      messages.error(request, error_message)
      return render(request, template_name=self.template)

    
class SignInView(View):
  template = 'accounts/signin.html'

  def get(self, request, *args, **kwargs):

    return render(request, template_name=self.template)

  def post(self, request, *args, **kwargs):
    username_or_email = request.POST.get('username_or_email')
    password = request.POST.get('password')


    try:
      user = User.objects.get(Q(username=username_or_email) | Q(email=username_or_email))
      user = authenticate(request, email=username_or_email, password=password)

      if user is not None:
        login(request, user)
        user.is_logged_in = True
        user.save()
      
        messages.success(request, f'Signed in as {user.username}')
        return redirect('home')
      
      else:
        messages.error(request, 'Incorrect password.')
        return render(request, template_name=self.template)
      
    except User.DoesNotExist:
      print('## Error: Invalid credentials.')
      messages.error(request, f'Invalid credentials.')
      return render(request, template_name=self.template)

def signout(request):
  if 'signout' in request.POST.get('command'):
    user = request.user
    print('## Is user logged in: ', user.is_logged_in)
    if user.is_authenticated:
      user.is_logged_in = False
      user.save()
      logout(request)
      print('## Is user logged in: ', user.is_logged_in)
      messages.success(request, f'Signout of {user.username}')
      return redirect('signin')
    else:
      messages.error(request, 'Error: Invalid request')
      return redirect('signin')

class HomeView(View):
  template = 'accounts/home.html'
  
  def get(self, request, *args, **kwargs):

    return render(request, template_name=self.template)
