from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from rest_framework_simplejwt import views as jwt_view

from .views import TermsOfUseView, UserRegisterView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('registrar/', UserRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('termos-de-uso', TermsOfUseView.as_view(), name='terms_use'),

    path('api/v1/token/', jwt_view.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', jwt_view.TokenRefreshView.as_view(), name='token_refresh'),
]
