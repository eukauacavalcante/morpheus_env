import smtplib

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from notifications.utils.colors import print_error, print_warning
from notifications.utils.send_email import send_oauth_email


@receiver(post_save, sender=User)
def send_email_user(sender, instance, created, **kwargs):
    if created and instance.email:
        try:
            if settings.EMAIL_MODE:
                send_oauth_email(instance)
            else:
                print('=' * 50)
                print('NOVO USUÁRIO\n')
                print_warning('[ATENÇÃO] Email automático desativado\n')
                print(f'Destinatário: {instance.first_name}')
                print(f'Endereço: {instance.email}')
                print('=' * 50)
        except smtplib.SMTPException as e:
            print('=' * 50)
            print('NOVO USUÁRIO\n')
            print_error('[ERRO] Falha ao tentar enviar email\n')
            print(f'Destinatário: {instance.first_name}')
            print(f'Endereço: {instance.email}')
            print(f"Detalhes do erro: {e}")
            print('=' * 50)
