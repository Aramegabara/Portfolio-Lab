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
    path('login/', Login.as_view(), name='login'),
    path('registration/', Register.as_view(), name='register'),
]