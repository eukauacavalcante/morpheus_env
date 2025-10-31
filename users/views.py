from django.contrib.auth.models import User
from django.shortcuts import render
from django.template import Context, Template
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views import generic

from .forms import CustomUserCreationForm, UserModelForm
from .models import TermsOfUseAndPrivacyPolicy


class UserRegisterView(generic.CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'


class UserDetailView(generic.DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user'


class UserUpdateView(generic.UpdateView):
    model = User
    form_class = UserModelForm
    template_name = 'user_update.html'

    def get_success_url(self):
        return reverse_lazy('user_detail', kwargs={'pk': self.object.pk})


class UserDeleteView(generic.DeleteView):
    model = User
    template_name = 'user_delete.html'
    success_url = '/accounts/login/'


class TermsOfUseView(generic.TemplateView):
    template_name = 'terms_of_use.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        terms = TermsOfUseAndPrivacyPolicy.objects.filter(is_active=True).last()
        if terms:
            template = Template(terms.content)
            rendered_content = template.render(
                Context({
                    'user': self.request.user,
                })
            )
            context['terms_and_policy'] = mark_safe(rendered_content)
        else:
            context['terms_and_policy'] = 'Termos não disponíveis'
        return context


def custom_lockout(request, credentials, *args, **kwargs):
    context = {'blocked': True}
    return render(request, 'registration/login.html', context, status=403)
