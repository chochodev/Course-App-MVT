import pytest
import sys
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from apps.accounts.tests.conftest import new_user, create_signup_data
from apps.accounts.models import User


class TestAuth:
    @pytest.mark.django_db
    def test_signup_user(self, client, create_signup_data):
        url = reverse('signup')
        # Follow == redirects
        response = client.post(url, data=create_signup_data, follow=True) 
        assert response.status_code == 200
        assert User.objects.filter(first_name=create_signup_data['first_name']).exists()

    @pytest.mark.django_db
    def test_signin_user(self, client, new_user, create_signin_data):
        # Creates a user before signing in
        user = new_user
        url = reverse('signin')
        response = client.post(url, create_signin_data)

        # Checks if user.is_active == True
        User = get_user_model()
        signed_in_user = User.objects.get(pk=client.session['_auth_user_id'])
        assert signed_in_user.is_active is True

        # Checks if the response redirects the user
        assert response.status_code in [200, 302]

    # @pytest.mark.django_db
    # def test_signout_user(self, client, create_signin_data):
    #     url = reverse('signin')
    #     client.post(url, create_signin_data, follow=True)

    #     # Checks if user.is_active == True
    #     User = get_user_model()
    #     user = User.objects.get(pk=client.session['_auth_user_id'])

    #     url = reverse('signout')
    #     response = client.get(url, follow=True)

    #     user = User.objects.get(pk=client.session['_auth_user_id'])

    #     assert user.is_active is False

    #     assert response.status_code == 302
