from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views import generic
from django_ratelimit.decorators import ratelimit
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .services import num_converter
from .services.ai_analysis import get_ai_analysis
from .services.system_metrics import get_system_status


class SystemAnalysisView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'system_analysis.html'


@method_decorator(ratelimit(key='user', rate='20/m', method='GET'), name='dispatch')
class SystemAnalysisAPIView(APIView):
    def get(self, request, *args, **kwargs):
        if getattr(request, 'limited', False):
            return Response(
                {'details': 'Limite de requisições excedidos! Tente novamente mais tarde.'},
                status=status.HTTP_429_TOO_MANY_REQUESTS,
            )
        data = get_system_status()
        return Response({'data': data}, status=status.HTTP_200_OK)


@method_decorator(ratelimit(key='user', rate='10/m', method='GET'), name='dispatch')
class AiAPIView(APIView):
    ERROR_MSG = '<p class="text-sm md:text-xl text-red-500">A análise por IA está indisponível no momento :(<br>Possível manutenção ocorrendo no sistema. Tente mais tarde!</p>'

    def get(self, request, *args, **kwargs):
        if getattr(request, 'limited', False):
            Response(
                {'details': 'Limite de requisições excedidos! Tente novamente mais tarde.'},
                status=status.HTTP_429_TOO_MANY_REQUESTS,
            )
        ai_response = get_ai_analysis() if settings.AI_MODE else self.ERROR_MSG
        return Response({'ai': ai_response}, status=status.HTTP_200_OK)


class NumberConverterView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'num_converter.html'


class NumberConverterAPIView(APIView):
    def get(self, request, *args, **kwargs):
        operation = request.GET.get('type')
        value = request.GET.get('value')
        CONVERTERS = {
            'bin2dec': lambda v: num_converter.bin_to_dec(v),
            'dec2bin': lambda v: num_converter.dec_to_bin(int(v)),
            'dec2hex': lambda v: num_converter.dec_to_hex(int(v)),
            'dec2oct': lambda v: num_converter.dec_to_oct(int(v)),
            'hex2dec': lambda v: num_converter.hex_to_dec(v),
            'oct2dec': lambda v: num_converter.oct_to_dec(v),
            'and': lambda v: int(request.GET.get('value1')) & int(request.GET.get('value2')),
            'or': lambda v: int(request.GET.get('value1')) | int(request.GET.get('value2')),
            'xor': lambda v: int(request.GET.get('value1')) ^ int(request.GET.get('value2')),
        }
        try:
            func = CONVERTERS.get(operation)
            result = func(value)
            return Response({'result': result}, status=status.HTTP_200_OK)
        except (ValueError, TypeError):
            return Response(
                {'result': 'Error ao calcular'},
                status=status.HTTP_400_BAD_REQUEST,
            )
