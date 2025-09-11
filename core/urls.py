from django.contrib import admin
from django.urls import path, include

from .views import tela_inicial


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tela_inicial, name='main'),
    path('sistema/', include('users.urls')),
]
