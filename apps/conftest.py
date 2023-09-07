import pytest 

@pytest.fixture
def create_user_data():
  user = {
    'first_name':'Emmanuel',
    'last_name':'Michael',
    'username':'chocho',
    'email':'chocho@gmail.com',
    'password1':'ilovethis',
    'password2':'ilovethis'
  }
  return user