from django.urls import path

from .views import (AiAPIView, NumberConverterAPIView, NumberConverterView,
                    SystemAnalysisAPIView, SystemAnalysisView)

urlpatterns = [
    path('monitoramento/', SystemAnalysisView.as_view(), name='system_data'),
    path('monitoramento/metrics/api', SystemAnalysisAPIView.as_view(), name='system_data_api'),
    path('monitoramento/ai/api', AiAPIView.as_view(), name='ai_api'),
    path('conversor/', NumberConverterView.as_view(), name='num_converter'),
    path('conversor/api/', NumberConverterAPIView.as_view(), name='num_converter_api'),
]
