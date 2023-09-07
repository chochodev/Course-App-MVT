import pytest
from django.urls import reverse
from apps.accounts.forms import UserCreationForm
from apps.conftest import create_user_data
from apps.accounts.models import User
from django.conf import settings


class TestAccount:
  signup_url = reverse('signup')
  signin_url = reverse('signin')
  home_url = reverse('home')
  signup_form = UserCreationForm


  @pytest.mark.django_db
  def test_signup_user(self, client, create_user_data):
    # FOR GET REQUEST
    response = client.get(self.signup_url)
    form = response.context['form']

    assert isinstance(form, self.signup_form)
    assert response.status_code in [200, 302]

    # FOR POST REQUEST
    user = create_user_data
    user['username'] = 'ilovethis01'   # To test the invalid credentials error messages
    print('User: ', user['username'], user['email'], user['password1'], user['password2'])

    res = client.post(
      self.signup_url, 
      data=create_user_data
    )
    
    # assert 'email' in form.errors
    # users = User.objects.all()
    # assert len(users) > 0
    
    # new_user = User.objects.get(username='chocho')
    # assert new_user

    assert res.status_code in [200, 302]