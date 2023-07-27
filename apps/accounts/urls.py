from django.urls import path
from apps.accounts import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
