from django.urls import path
from .views import system_analysis_view, number_converter_page, number_converter_api

urlpatterns = [
    path('monitoramento/', system_analysis_view, name='system_data'),
    path('conversor/', number_converter_page, name='num_converter'),
    path('conversor/api/', number_converter_api, name='num_converter_api'),
]
