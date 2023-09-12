from django.urls import path
from apps.accounts.views import *

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('home/', HomeView.as_view(), name='home'),
    # path('signout/', SignOutView.as_view(), name='signout'),
]
