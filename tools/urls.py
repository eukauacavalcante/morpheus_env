from django.urls import path
from .views import SystemAnalysisView, system_analysis_api_view, ai_api_view, NumberConverterView, number_converter_api

urlpatterns = [
    path('monitoramento/', SystemAnalysisView.as_view(), name='system_data'),
    path('monitoramento/metrics/api', system_analysis_api_view, name='system_data_api'),
    path('monitoramento/ai/api', ai_api_view, name='ai_api'),
    path('conversor/', NumberConverterView.as_view(), name='num_converter'),
    path('conversor/api/', number_converter_api, name='num_converter_api'),
]
