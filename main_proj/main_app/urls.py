from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import (
    LandingPage,
    AddDonation,
    Login,
    Register,
    )

urlpatterns = [
    path('', LandingPage.as_view(), name='start'),
    path('donat/', AddDonation.as_view(), name='donat'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('login/', Login.as_view(), name='login'),
    path('registration/', Register.as_view(), name='register'),
]