import pytest
from django.urls import reverse
from apps.accounts.forms import UserCreationForm
from apps.conftest import signup_user_data, signin_user_data
from apps.accounts.models import User
from django.conf import settings
import re


class TestAccount:
  signup_url = reverse('signup')
  signin_url = reverse('signin')
  home_url = reverse('home')
  signup_form = UserCreationForm


  @pytest.mark.django_db
  def test_signup_user(self, client, signup_user_data):
    # FOR GET REQUEST
    response = client.get(self.signup_url)
    form = response.context['form']

    assert isinstance(form, self.signup_form)
    assert response.status_code in [200, 302]

    # FOR POST REQUEST
    user = signup_user_data

    # TO TEST ERROR MESSAGES
    test_error_messages = False
    if test_error_messages == True:
      user['email'] = '1234ert5r4'  # To test the invalid credentials error messages
      res = client.post(
        self.signup_url, 
        data=user,
        follow=True
      ) 
      signup_messages = res.context['messages']
      
      for message in signup_messages:
        assert form.fields['email'].error_messages['invalid'] in message.message
        return

    # TO TEST VALID FORM SUBMISSION
    res = client.post(
      self.signup_url, 
      data=user,
      follow=True
    )
    users = User.objects.all()

    assert len(users) > 0 # Test if number of users increased
    assert User.objects.get(username=user['username']) # Test if username in the db
    assert res.status_code in [200, 302]

  @pytest.mark.django_db
  def test_signin_user(self, client, signup_user_data, signin_user_data):
    # FOR GET REQUEST
    get_res = client.get(self.signin_url)
    
    assert get_res.status_code in [200, 302]

    # FOR POST REQUEST
    signed_up_user = self.test_signup_user(client, signup_user_data)
    assert User.objects.get(email=signup_user_data['email'])

    # User check
    user1 = User.objects.all()[0]
    print('## User:', user1)
    
    user = signin_user_data
    post_res = client.post(
      self.signin_url,
      data=user,
      follow=True
    )

    signin_messages = post_res.context['messages']
    for message in signin_messages:
      print('## Test message: ', message.message)

    signed_in_user = User.objects.get(email=user['username_or_email'])
    assert signed_in_user
    assert signed_in_user.is_logged_in is True

    print('## Testing RES: ', post_res)
    assert post_res.status_code in [200, 302]