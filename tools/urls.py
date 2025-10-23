from django.urls import path

from .views import (AiAPIView, NumberConverterAPIView, NumberConverterView,
                    SystemAnalysisAPIView, SystemAnalysisView)

urlpatterns = [
    path('monitoramento/', SystemAnalysisView.as_view(), name='system_data'),
    path('monitoramento/api/v1/metrics', SystemAnalysisAPIView.as_view(), name='system_data_api'),
    path('monitoramento/api/v1/ai', AiAPIView.as_view(), name='ai_api'),
    path('conversor/', NumberConverterView.as_view(), name='num_converter'),
    path('conversor/api/v1/converter', NumberConverterAPIView.as_view(), name='num_converter_api'),
]
