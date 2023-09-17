from django.urls import path
from apps.static_pages.views import *

urlpatterns = [
  path('about/', about_page, name='about'),
  path('privacy/', privacy_page, name='privacy'),
  path('policy/', policy_page, name='policy'),
]
