import pytest 

@pytest.fixture
def signup_user_data():
  user = {
    'first_name':'Emmanuel',
    'last_name':'Michael',
    'username':'chocho',
    'email':'chocho@gmail.com',
    'password1':'ilovethis',
    'password2':'ilovethis'
  }
  return user

@pytest.fixture
def signin_user_data():
  user = {
    'username_or_email':'chocho@gmail.com',
    'password':'ilovethis'
  }
  return user