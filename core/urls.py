from django.contrib import admin
from django.urls import include, path

from .views import HomeView, StudentsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('informacoes-do-software/', StudentsView.as_view(), name='students'),
    path('accounts/', include('users.urls')),
    path('sistema/', include('tools.urls')),
]
