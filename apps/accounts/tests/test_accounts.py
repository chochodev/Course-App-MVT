import pytest
from django.urls import reverse
from apps.accounts.tests.conftest import create_user, create_user_data
from apps.accounts.models import User

# def test_lorem():
#     assert 1 == 1

class TestAuth:
    @pytest.mark.django_db
    def test_signup_user(self, client, create_user_data):
        url = reverse('signup')
        response = client.post(url, data=create_user_data, follow=True) # Follow is to follow redirects
        assert response.status_code == 200
        assert User.objects.filter(first_name=create_user_data['first_name']).exists