from http import HTTPStatus

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.views import generic

from .services import num_converter
from .services.ai_analysis import get_analysis
from .services.system_metrics import get_system_stats


class SystemAnalysisView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'system_analysis.html'


@login_required
def system_analysis_api_view(request):
    if request.method == 'GET':
        data = get_system_stats()
        return JsonResponse({'data': data})
    else:
        return HttpResponse(
            '<h1>Método não permitido</h1>',
            status=HTTPStatus.METHOD_NOT_ALLOWED
        )


if settings.AI_MODE:
    @login_required
    def ai_api_view(request):
        if request.method == 'GET':
            ai_response = get_analysis()
            print(ai_response)
            return JsonResponse({'ai': ai_response})
        else:
            return HttpResponse(
                '<h1>Método não permitido</h1>',
                status=HTTPStatus.METHOD_NOT_ALLOWED
            )
else:
    @login_required
    def ai_api_view(request):
        if request.method == 'GET':
            ai_response = '<p class="text-xl text-red-500">A análise por IA está indisponível no momento :(<br>Possível manutenção ocorrendo no sistema. Tente mais tarde!</p>'
            return JsonResponse({'ai': ai_response})
        else:
            return HttpResponse(
                '<h1>Método não permitido</h1>',
                status=HTTPStatus.METHOD_NOT_ALLOWED
            )


class NumberConverterView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'num_converter.html'


@login_required
def number_converter_api(request):
    if request.method == 'GET':
        type = request.GET.get('type')
        value = request.GET.get('value')

        match(type):
            case 'bin2dec':
                result = num_converter.bin_to_dec(value)
            case 'dec2bin':
                result = num_converter.dec_to_bin(int(value))
            case 'dec2hex':
                result = num_converter.dec_to_hex(int(value))
            case 'dec2oct':
                result = num_converter.dec_to_oct(int(value))
            case 'hex2dec':
                result = num_converter.hex_to_dec(value)
            case 'oct2dec':
                result = num_converter.oct_to_dec(value)
            case 'and':
                value1 = int(request.GET.get('value1'))
                value2 = int(request.GET.get('value2'))
                result = value1 & value2
            case 'or':
                value1 = int(request.GET.get('value1'))
                value2 = int(request.GET.get('value2'))
                result = value1 | value2
            case 'xor':
                value1 = int(request.GET.get('value1'))
                value2 = int(request.GET.get('value2'))
                result = value1 ^ value2

        return JsonResponse({'result': result})
    else:
        return HttpResponse(
            '<h1>Método não permitido</h1>',
            status=HTTPStatus.METHOD_NOT_ALLOWED
        )
