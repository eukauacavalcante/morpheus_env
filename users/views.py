from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm


class UserRegisterView(generic.CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')


class TermsOfUseView(generic.TemplateView):
    template_name = 'terms_of_use.html'
