from django.urls import path
from apps.accounts.views import SignUpView, SignInView, home

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('home/', home, name='home')
]
