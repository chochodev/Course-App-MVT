from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
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
    username_or_email = request.POST.get('username_or_email', '')
    password = request.POST.get('password', '')

    print('## Username or Email: ', username_or_email, '\n## Password: ', password)
    try:
      user = User.objects.get(Q(username=username_or_email) | Q(email=username_or_email))
      if not check_password(password, user.password):
        messages.error(request, 'Incorrect password')
        return render(request, template_name=self.template)
      
      else:
        print('## Username: ', user.username)
        user = authenticate(request, username=user.username, password=password)
        print('## Authenticate user:', user)
        
    except User.DoesNotExist:
      messages.error(request, f'Invalid Username or Emails.')
      return render(request, template_name=self.template)
    
    if user is not None:
      login(request, user)
      user.is_logged_in = True
      user.save()
  
      messages.success(request, f'Signed in as {user.username}')
      return redirect('home')
    else:
      messages.error(request, 'Error occured during signin.')
      return render(request, template_name=self.template)
    
class HomeView(View):
  template = 'accounts/home.html'
  
  def get(self, request, *args, **kwargs):

    return render(request, template_name=self.template)
