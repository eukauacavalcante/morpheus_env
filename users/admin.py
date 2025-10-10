from django.contrib import admin
from django.contrib.auth import get_user_model

from notifications.utils.send_email import send_update_terms_email

from .models import TermsOfUseAndPrivacyPolicy

User = get_user_model()


@admin.register(TermsOfUseAndPrivacyPolicy)
class TermsAndPrivacyAdmin(admin.ModelAdmin):
    list_display = ('id', 'updated_at', 'is_active')
    actions = ['send_terms_update_email']

    def send_terms_update_email(self, request):
        users = User.objects.all()
        for user in users:
            send_update_terms_email(user)
        self.message_user(request, "E-mails enviados com sucesso!")
        print('\nEmail enviado à todos!\n')
    send_terms_update_email.short_description = "Enviar e-mail de atualização para todos os usuários"
