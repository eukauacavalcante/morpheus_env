from django.contrib import admin
from django.urls import path, include

from .views import main_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='main'),
    path('sistema/', include('users.urls')),
]
