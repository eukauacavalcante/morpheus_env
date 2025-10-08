from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views import generic

from .services import num_converter
from .services.ai_analysis import get_ai_analysis
from .services.system_metrics import get_system_status


class SystemAnalysisView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'system_analysis.html'


class SystemAnalysisAPIView(LoginRequiredMixin, generic.View):
    def get(self, request, *args, **kwargs):
        data = get_system_status()
        return JsonResponse({'data': data})


class AiAPIView(LoginRequiredMixin, generic.View):
    ERROR_MSG = (
        '<p class="text-xl text-red-500">A análise por IA está indisponível no momento :(<br>Possível manutenção ocorrendo no sistema. Tente mais tarde!</p>'
    )

    def get(self, request, *args, **kwargs):
        ai_response = get_ai_analysis() if settings.AI_MODE else self.ERROR_MSG
        return JsonResponse({'ai': ai_response})


class NumberConverterView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'num_converter.html'


class NumberConverterAPIView(LoginRequiredMixin, generic.View):
    def get(self, request, *args, **kwargs):
        operation = request.GET.get('type')
        value = request.GET.get('value')
        converters = {
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
            func = converters.get(operation)
            result = func(value)
            return JsonResponse({'result': result})
        except (ValueError, TypeError):
            return JsonResponse({'result': 'Error ao calcular'}, status=400)
