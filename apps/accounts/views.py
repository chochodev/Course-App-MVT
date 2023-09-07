from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from django.contrib import messages
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
    print('## Post request made')
    if form.is_valid():
      user = form.save()
      print('## Form is valid')
      messages.success(request, f'Account has been created for {user.username}')
      return redirect('home')
    else:
      print('## Form is invalid')
      error_messages = form.errors.items
      if error_messages:
        for field, errors in error_messages:
            for error in errors:
              print('## Field, Error: ', field, error)
              error_message = error
      else:
        error_message = 'An error occured with your submission.'

      print('## Error: ', error_message)
      messages.error(request, error_message)
      return redirect('signup')

    
class SignInView(View):
  def get(self, request, *args, **kwargs):
    template = 'accounts/signin.html'
    render(request, template_name=self.template)
  def post(self, request, *args, **kwargs):
    username_or_password = request.POST.get('username_or_password')
    password = request.POST.get('password')

    try:
      user = User.objects.get(username=username_or_password)
      user = authenticate(request, username=username_or_password, password=password)
    except User.DoesNotExist:
      user = authenticate(request, email=username_or_password, password=password)
    finally:
      if user is not None:
        login(request, user)
        user.is_active = True
        user.save()
        return redirect('home')
      else:
        messages.error(request, '')

def home(request):
  pass