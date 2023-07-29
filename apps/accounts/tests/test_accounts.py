import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from apps.accounts.tests.conftest import create_user, create_user_data
from apps.accounts.models import User


class TestAuth:
    @pytest.mark.django_db
    def test_signup_user(self, client, create_user_data):
        url = reverse('signup')
        response = client.post(url, data=create_user_data, follow=True) # Follow is to follow redirects
        assert response.status_code == 200
        assert User.objects.filter(first_name=create_user_data['first_name']).exists

    @pytest.mark.django_db
    def test_signin_user(self, client, create_login_data):
        url = reverse('signin')
        response = client.post(url, create_login_data)

        # Checks if user.is_active == True
        User = get_user_model()
        user = User.objects.get(pk=client.session['_auth_user_id'])

        # Check if user.is_active is True
        assert user.is_active is True

        # Checks if the response redirects the user
        assert response.status_code == 200 or 302

    @pytest.mark.django_db
    def test_signout_user(self, client, create_login_data):
        url = reverse('signin')
        client.post(url, create_login_data, follow=True)

        # Checks if user.is_active == True
        User = get_user_model()
        user = User.objects.get(pk=client.session['_auth_user_id'])

        url = reverse('signout')
        response = client.get(url, follow=True)

        user = User.objects.get(pk=client.session['_auth_user_id'])

        assert user.is_active is False

        assert response.status_code == 302
