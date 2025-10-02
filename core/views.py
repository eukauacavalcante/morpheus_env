from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'index.html'


class StudentsView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'students.html'
