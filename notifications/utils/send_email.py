import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.conf import settings

from .email_oauth2 import get_oauth2_string
from .logs import log_user_creation


def get_date_format():
    date = datetime.now().strftime('%d/%m/%Y')
    return date


def send_oauth_email(user):
    try:
        auth_string = get_oauth2_string(
            settings.EMAIL_HOST_USER,
            settings.GOOGLE_OAUTH2_CLIENT_ID,
            settings.GOOGLE_OAUTH2_CLIENT_SECRET,
            settings.GOOGLE_OAUTH2_REFRESH_TOKEN,
        )
        date = get_date_format()
        body_text = (
            f'Olá, {user.first_name}! Obrigado por se cadastrar e utilizar o Morpheus Env.'
            ' Este projeto foi desenvolvido com fins acadêmicos — voltado à pesquisa, aprendizado e demonstração de conceitos.'
            ' Por isso, pedimos que os resultados e recursos do sistema não sejam interpretados como serviços profissionais ou comerciais.'
            ' Estamos felizes em tê-lo(a) conosco!'
        )
        body_html = f"""
        <html>
            <h1>Olá, <strong>{user.first_name}</strong>!</h1>
            <p>Obrigado por se cadastrar e utilizar o <strong>Morpheus Env</strong>! Este projeto foi desenvolvido com fins acadêmicos —
            voltado à pesquisa, aprendizado e demonstração de conceitos.</p>
            <p>Por isso, pedimos que os resultados e recursos do sistema não sejam interpretados como serviços profissionais ou comerciais.</p>
            <p>Estamos felizes em tê-lo(a) conosco!</p>
            <p>Equipe Morpheus Env, {date}.</p>
        </html>
        """

        msg = MIMEMultipart('alternative')
        msg['Subject'] = 'Bem-vindo(a) ao Morpheus Env'
        msg['From'] = settings.DEFAULT_FROM_EMAIL
        msg['To'] = f'{user.email}'
        msg.attach(MIMEText(body_text, 'plain'))
        msg.attach(MIMEText(body_html, 'html'))

        with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.docmd('AUTH', 'XOAUTH2 ' + auth_string)
            server.send_message(msg)
            log_user_creation(user)

    except smtplib.SMTPException as e:
        log_user_creation(user, error=str(e))

