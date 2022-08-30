from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('home', home, name='home'),
    path('sign-up', sign_up, name='sign_up'),
    path('create-complaint', create_complaint, name='create_complaint'),
    path('update_profile', update_profile, name='update_profile'),
    path('dashboard', dashboard, name='dashboard'),
]
