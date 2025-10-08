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
            ' Este projeto foi desenvolvido com fins experimentais e acadêmicos — voltado à pesquisa, aprendizado e demonstração de conceitos.'
            ' Por isso, pedimos que os resultados e recursos do sistema não sejam interpretados como serviços profissionais ou comerciais.'
            '\nPara conhecer mais sobre o projeto, acesse nosso repositório oficial: https://github.com/eukauacavalcante/morpheus_env'
            '\nCaso tenha sugestões de melhorias ou precise reportar algum problema, entre em contato conosco através do e-mail: morpheusenv@gmail.com'
            '\nEstamos felizes em tê-lo(a) conosco!'
            f'\nEquipe Morpheus Env, {date}'
        )
        body_html = f"""
            <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333333; max-width: 600px; margin: 0 auto; padding: 20px;">
                <div style="background-color: #f8f9fa; border-radius: 8px; padding: 30px; border-left: 4px solid #4a90e2;">
                    <h2 style="color: #2c3e50; margin-top: 0;">Olá, {user.first_name}!</h2>
                    <p style="margin-bottom: 15px;">
                        Obrigado por se cadastrar e utilizar o <strong>Morpheus Env</strong>.
                    </p>
                    <p style="margin-bottom: 15px;">
                        Este projeto foi desenvolvido com fins <strong>experimentais e acadêmicos</strong> — voltado à pesquisa, aprendizado e demonstração de conceitos. Por isso, pedimos que os resultados e recursos do sistema não sejam interpretados como serviços profissionais ou comerciais.
                    </p>
                    <div style="background-color: #ffffff; border-radius: 6px; padding: 20px; margin: 20px 0; border: 1px solid #e0e0e0;">
                        <p style="margin-bottom: 10px; font-weight: bold; color: #4a90e2;">📚 Conheça mais sobre o projeto:</p>
                        <p style="margin-bottom: 0;">
                            <a href="https://github.com/eukauacavalcante/morpheus_env"
                            style="color: #4a90e2; text-decoration: none; font-weight: 500;"
                            target="_blank">
                                https://github.com/eukauacavalcante/morpheus_env
                            </a>
                        </p>
                    </div>
                    <div style="background-color: #ffffff; border-radius: 6px; padding: 20px; margin: 20px 0; border: 1px solid #e0e0e0;">
                        <p style="margin-bottom: 10px; font-weight: bold; color: #4a90e2;">💬 Sugestões ou problemas?</p>
                        <p style="margin-bottom: 0;">
                            Entre em contato conosco através do e-mail:
                            <a href="mailto:morpheusenv@gmail.com"
                            style="color: #4a90e2; text-decoration: none; font-weight: 500;">
                                morpheusenv@gmail.com
                            </a>
                        </p>
                    </div>
                    <p style="margin-bottom: 0; margin-top: 25px; color: #2c3e50; font-weight: 500;">
                        Estamos felizes em tê-lo(a) conosco! 🚀
                    </p>
                    <p style="margin-bottom: 0; margin-top: 5px; color: #2c3e50; font-weight: 500;">
                        Equipe Morpheus Env, {date}.
                    </p>
                </div>
                <div style="text-align: center; margin-top: 30px; padding-top: 20px; border-top: 1px solid #e0e0e0;">
                    <p style="color: #888888; font-size: 12px; margin: 0;">
                        © Morpheus Env - Projeto Acadêmico e Experimental
                    </p>
                </div>
            </body>
            </html>
            """

        msg = MIMEMultipart('alternative')
        msg['Subject'] = 'Bem-vindo(a) ao Morpheus Env'
        msg['From'] = settings.DEFAULT_FROM_EMAIL
        msg['To'] = user.email
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

