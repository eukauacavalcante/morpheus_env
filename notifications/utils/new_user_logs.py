from notifications.utils.colors import (print_error, print_success,
                                        print_warning)


def log_user_creation(user, email_sent=True, error=None):
    print('=' * 50)
    print('NOVO USUÁRIO\n')
    if error:
        print_error('[ERRO] Falha ao tentar enviar e-mail')
        print(f"Detalhes do erro: {error}")
    if not email_sent:
        print_warning('[ATENÇÃO] Email automático desativado\n')
    else:
        print_success('[SUCESSO] Email enviado')
    print(f'Destinatário: {user.first_name} ({user.username})')
    print(f'Endereço: {user.email}')
    print('=' * 50)
