import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.conf import settings

from .email_oauth2 import get_oauth2_string
from .emails import (EMAIL_NEW_USER_HTML, EMAIL_NEW_USER_TEXT,
                     EMAIL_TERMS_UPDATED)
from .new_user_logs import log_user_creation


def get_date_format():
    date = datetime.now().strftime('%d/%m/%Y')
    return date


def get_auth_string():
    return get_oauth2_string(
        email=settings.EMAIL_HOST_USER,
        client_secret=settings.GOOGLE_OAUTH2_CLIENT_ID,
        client_id=settings.GOOGLE_OAUTH2_CLIENT_SECRET,
        refresh_token=settings.GOOGLE_OAUTH2_REFRESH_TOKEN,
    )


def create_email_message(subject, user_email, body_text, body_html):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = settings.DEFAULT_FROM_EMAIL
    msg['To'] = user_email
    msg.attach(MIMEText(body_text, 'plain'))
    msg.attach(MIMEText(body_html, 'html'))
    return msg


def send_email_via_oauth(msg):
    auth_string = get_auth_string()

    with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.docmd('AUTH', 'XOAUTH2 ' + auth_string)
        server.send_message(msg)


def send_update_terms_email(user):
    try:
        date = get_date_format()
        body_text = 'Teste'
        body_html = EMAIL_TERMS_UPDATED.format(user_first_name=user.first_name, date=date)
        msg = create_email_message(
            subject='Atualização dos Termos de Uso e Política de Privacidade',
            user_email=user.email,
            body_text=body_text,
            body_html=body_html,
        )
        send_email_via_oauth(msg)

    except smtplib.SMTPException as e:
        print(f'\nErro: {e}\n')


def send_new_user_email(user):
    try:
        date = get_date_format()
        body_text = EMAIL_NEW_USER_TEXT.format(user_first_name=user.first_name, date=date)
        body_html = EMAIL_NEW_USER_HTML.format(user_first_name=user.first_name, date=date)
        msg = create_email_message(
            subject='Bem-vindo(a) ao Morpheus Env',
            user_email=user.email,
            body_text=body_text,
            body_html=body_html,
        )
        send_email_via_oauth(msg)
        log_user_creation(user)

    except smtplib.SMTPException as e:
        log_user_creation(user, error=str(e))
