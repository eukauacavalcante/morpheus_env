from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from rest_framework_simplejwt import views as jwt_view

from .views import (
    TermsOfUseView,
    UserDeleteView,
    UserDetailView,
    UserRegisterView,
    UserUpdateView,
)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('registrar/', UserRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('perfil/<int:pk>', UserDetailView.as_view(), name='user_detail'),
    path('perfil/<int:pk>/atualizar-conta', UserUpdateView.as_view(), name='user_update'),
    path('perfil/<int:pk>/deletar-conta', UserDeleteView.as_view(), name='user_delete'),
    path('termos-de-uso', TermsOfUseView.as_view(), name='terms_use'),
    path('api/v1/token/', jwt_view.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', jwt_view.TokenRefreshView.as_view(), name='token_refresh'),
]
