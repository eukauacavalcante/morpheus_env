import smtplib

from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from notifications.utils.new_user_logs import log_user_creation
from notifications.utils.send_email import send_oauth_email


@receiver(post_save, sender=User)
def send_email_user(sender, instance, created, **kwargs):
    if created and instance.email:
        try:
            if settings.EMAIL_MODE:
                send_oauth_email(instance)
            else:
                log_user_creation(instance, email_sent=False)
        except smtplib.SMTPException as e:
            log_user_creation(instance, error=str(e))
