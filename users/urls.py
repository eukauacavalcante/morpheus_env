from django.urls import path

from .views import system_dashboard


urlpatterns = [
    path('', system_dashboard, name='system_data'),
]
