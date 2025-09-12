from django.urls import path
from .views import home_view, profile_view, edit_profile_image_view

urlpatterns = [
    path('', home_view, name='home'),
    path('accounts/profile/', profile_view, name='account_profile'),
    path('accounts/edit_profile/', edit_profile_image_view, name='edit_profile'),
]
