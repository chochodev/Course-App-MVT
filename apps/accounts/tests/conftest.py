import pytest
from apps.accounts.models import User

@pytest.fixture
def create_signup_data():
    return {
        'first_name': 'mikey',
        'last_name': 'chocho',
        'email': 'chocho12@gmail.com',
        'username': 'user_chocho',
        'password1': 'ilovethis',
        'password2': 'ilovethis',
    }

@pytest.fixture
def create_signin_data():
    return {
        'email': 'chocho12@gmail.com',
        'password': 'ilovethis',
    }

########################################################

@pytest.fixture
def create_user_data():
    return {
        'first_name': 'mikey',
        'last_name': 'chocho',
        'email': 'chocho12@gmail.com',
        'username': 'user_chocho',
        'password': 'ilovethis',
    }

# Create new user into the database through the models
@pytest.fixture
def new_user(create_user_data):
    return User.objects.create(**create_user_data)