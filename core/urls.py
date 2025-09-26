from django.contrib import admin
from django.urls import path, include

from .views import main_view, students_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='main'),
    path('informacoes-do-software/', students_view, name='students'),
    path('accounts/', include('users.urls')),
    path('sistema/', include('tools.urls')),
]
