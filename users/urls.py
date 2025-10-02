from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import UserRegisterView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('registrar/', UserRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
