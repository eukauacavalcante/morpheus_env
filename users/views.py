from django.contrib.auth.models import User
from django.template import Context, Template
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views import generic

from .forms import CustomUserCreationForm
from .models import TermsOfUseAndPrivacyPolicy


class UserRegisterView(generic.CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')


class TermsOfUseView(generic.TemplateView):
    template_name = 'terms_of_use.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        terms = TermsOfUseAndPrivacyPolicy.objects.filter(is_active=True).last()
        if terms:
            template = Template(terms.content)
            rendered_content = template.render(Context({
                'user': self.request.user,
            }))
            context['terms_and_policy'] = mark_safe(rendered_content)
        else:
            context['terms_and_policy'] = 'Termos não disponíveis'
        return context
