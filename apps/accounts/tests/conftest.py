import pytest
from apps.accounts.models import User

@pytest.fixture
def create_user_data():
    return {
        'first_name': 'mikey',
        'last_name': 'chocho',
        'email': 'chocho@gmail.com',
        'password1': 'ilovethis',
        'password2': 'ilovethis',
    }

@pytest.fixture
def create_user(create_user_data):
    return User.objects.create(**create_user_data)