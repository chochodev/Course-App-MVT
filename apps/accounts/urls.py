from django.urls import path
from apps.accounts import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signout/', views.SignOutView.as_view(), name='signout'),
    path('signin/', views.SignInView.as_view(), name='signin'),
    path('home/', views.SignInView.as_view(), name='home'),

]
