from django.urls import path

from .views import (AiAPIView, NumberConverterAPIView, NumberConverterView,
                    SystemAnalysisAPIView, SystemAnalysisView)

urlpatterns = [
    path('monitoramento/', SystemAnalysisView.as_view(), name='system_data'),
    path('monitoramento/v1/metrics-api', SystemAnalysisAPIView.as_view(), name='system_data_api'),
    path('monitoramento/v1/ai-api', AiAPIView.as_view(), name='ai_api'),
    path('conversor/', NumberConverterView.as_view(), name='num_converter'),
    path('conversor/v1/api', NumberConverterAPIView.as_view(), name='num_converter_api'),
]
