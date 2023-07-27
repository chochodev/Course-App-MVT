from django.urls import reverse
import pytest
from apps.accounts.tests.conftest import create_user
from apps.accounts.models import User

class AuthTest:
    def signup_user_test(self, client, create_user_data):
        url = reverse('signup')
        response = client.post(url, data=create_user_data, follow=True) # Follow is to follow redirects
        assert response.status_code == 200
        assert User.objects.filter(first_name=create_user_data['first_name']).exists