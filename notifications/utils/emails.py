# ========== NOVO USUÁRIO ==========

EMAIL_NEW_USER_TEXT = (
    'Olá, {user_first_name}!\n\n'
    'Obrigado por se cadastrar e utilizar o Morpheus Env.\n\n'
    'Este projeto foi desenvolvido com fins experimentais e acadêmicos – voltado à pesquisa, aprendizado e demonstração de conceitos. '
    'Por isso, pedimos que os resultados e recursos do sistema não sejam interpretados como serviços profissionais ou comerciais.\n\n'
    '📚 Conheça mais sobre o projeto:\n'
    'https://github.com/eukauacavalcante/morpheus_env\n\n'
    '💬 Sugestões ou problemas?\n'
    'Entre em contato conosco através do e-mail: morpheusenv@gmail.com\n\n'
    'Estamos felizes em tê-lo(a) conosco! 🚀\n\n'
    'Equipe Morpheus Env, {date}\n\n'
    '---\n'
    'Esta mensagem foi enviada para {user_email}.\n'
    'Se tiver dúvidas ou reclamações, fale conosco: morpheusenv@gmail.com\n'
    'Documentação: https://eukauacavalcante.github.io/morpheus_env\n'
    'Github: https://github.com/eukauacavalcante/morpheus_env\n'
    'Morpheus Env | João Pessoa, Paraíba, Brasil.\n'
    '© Morpheus Env - Projeto Acadêmico e Experimental'
)

EMAIL_NEW_USER_HTML = """
<html>
<body style="margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif; background-color: #f4f4f4;">
    <div style="max-width: 600px; margin: 0 auto; background-color: #ffffff;">
        <!-- Conteúdo Principal -->
        <div style="background-color: #ffffff; padding: 40px 30px; border-left: 4px solid #7f22fe;">
            <h2 style="color: #7f22fe; margin: 0 0 24px 0; font-size: 24px; font-weight: 600;">Olá, {user_first_name}!</h2>

            <p style="margin: 0 0 16px 0; color: #333333; font-size: 15px; line-height: 1.6;">
                Obrigado por se cadastrar e utilizar o <strong>Morpheus Env</strong>.
            </p>

            <p style="margin: 0 0 24px 0; color: #333333; font-size: 15px; line-height: 1.6;">
                Este projeto foi desenvolvido com fins <strong>experimentais e acadêmicos</strong> – voltado à pesquisa, aprendizado e demonstração de conceitos. Por isso, pedimos que os resultados e recursos do sistema não sejam interpretados como serviços profissionais ou comerciais.
            </p>

            <!-- Box: Conheça o Projeto -->
            <div style="background-color: #f8f9fa; border-radius: 8px; padding: 20px; margin: 0 0 16px 0; border-left: 3px solid #7f22fe;">
                <p style="margin: 0 0 10px 0; font-weight: 600; color: #7f22fe; font-size: 14px;">📚 Conheça mais sobre o projeto:</p>
                <p style="margin: 0;">
                    <a href="https://github.com/eukauacavalcante/morpheus_env" style="color: #4a90e2; text-decoration: none; font-size: 14px; word-break: break-all;" target="_blank">
                        github.com/eukauacavalcante/morpheus_env
                    </a>
                </p>
            </div>

            <div style="background-color: #f8f9fa; border-radius: 8px; padding: 20px; margin: 0 0 28px 0; border-left: 3px solid #7f22fe;">
                <p style="margin: 0 0 10px 0; font-weight: 600; color: #7f22fe; font-size: 14px;">💬 Sugestões ou problemas?</p>
                <p style="margin: 0; color: #333333; font-size: 14px; line-height: 1.6;">
                    Entre em contato conosco através do e-mail:
                    <a href="mailto:morpheusenv@gmail.com" style="color: #4a90e2; text-decoration: none; font-weight: 500;">
                        morpheusenv@gmail.com
                    </a>
                </p>
            </div>

            <p style="margin: 0 0 8px 0; color: #333333; font-size: 15px; font-weight: 500;">
                Estamos felizes em tê-lo(a) conosco! 🚀
            </p>

            <p style="margin: 0; color: #666666; font-size: 14px;">
                Equipe Morpheus Env, {date}
            </p>
        </div>

        <div style="background-color: #2d2d2d; padding: 30px 30px; border-left: 4px solid #7f22fe;">
            <h4 style="color: #ffffff; margin: 0 0 20px 0; font-size: 16px; font-weight: 600;">Morpheus Env</h4>

            <p style="color: #cccccc; font-size: 13px; line-height: 1.6; margin: 0 0 20px 0; text-align: center;">
                Esta mensagem foi enviada para <a href="mailto:{user_email}" style="color: #7f22fe; text-decoration: none;">{user_email}</a>.
                <br>
                Se tiver dúvidas ou reclamações, <a href="mailto:morpheusenv@gmail.com" style="color: #7f22fe; text-decoration: none; font-weight: 600;">fale conosco</a>.
            </p>

            <div style="margin: 0 0 20px 0; padding-top: 20px; border-top: 1px solid #444444; text-align: center;">
                <a href="https://eukauacavalcante.github.io/morpheus_env" style="color: #cccccc; text-decoration: none; font-size: 12px; font-weight: 600; margin-right: 8px;" target="_blank">Documentação</a>
                <span style="color: #666666; margin: 0 8px;">|</span>
                <a href="https://github.com/eukauacavalcante/morpheus_env" style="color: #cccccc; text-decoration: none; font-size: 12px; font-weight: 600; margin-left: 8px;" target="_blank">Github</a>
            </div>

            <p style="color: #999999; font-size: 12px; margin: 0 0 15px 0; text-align: center;">
                Morpheus Env | João Pessoa, Paraíba, Brasil
            </p>

            <div style="padding-top: 15px; border-top: 1px solid #444444; text-align: center;">
                <p style="color: #888888; font-size: 11px; margin: 0;">
                    © Morpheus Env - Projeto Acadêmico e Experimental
                </p>
            </div>
        </div>
    </div>
</body>
</html>
"""


# ========== TERMOS ATUALIZADOS ==========

EMAIL_TERMS_UPDATED_TEXT = (
    'Olá, {user_first_name}!\n\n'
    'Houve uma atualização nos nossos Termos de Uso e Política de Privacidade.\n\n'
    'Atualizamos os Termos de Uso e Política de Privacidade para explicar as ações do nosso sistema e oferecer mais informações. '
    'Os Termos e Política atualizados entram em vigor nesse momento para usuários existentes. '
    'Você pode ler o que mudou acessando Termos e Política na nossa tela inicial.\n\n'
    'Você não precisa fazer mais nada para concordar com os Termos e Política atualizados. '
    'Ao continuar usando o Morpheus Env, você aceita-os.\n\n'
    'Agradecemos a compreensão! 🚀\n\n'
    'Equipe Morpheus Env, {date}\n\n'
    '---\n'
    'Esta mensagem foi enviada para {user_email}.\n'
    'Se tiver dúvidas ou reclamações, fale conosco: morpheusenv@gmail.com\n'
    'Documentação: https://eukauacavalcante.github.io/morpheus_env\n'
    'Github: https://github.com/eukauacavalcante/morpheus_env\n'
    'Morpheus Env | João Pessoa, Paraíba, Brasil.\n'
    '© Morpheus Env - Projeto Acadêmico e Experimental'
)

EMAIL_TERMS_UPDATED_HTML = """
<html>
<body style="margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif; background-color: #f4f4f4;">
    <div style="max-width: 600px; margin: 0 auto; background-color: #ffffff;">
        <!-- Conteúdo Principal -->
        <div style="background-color: #ffffff; padding: 40px 30px; border-left: 4px solid #7f22fe;">
            <h2 style="color: #7f22fe; margin: 0 0 24px 0; font-size: 24px; font-weight: 600;">Olá, {user_first_name}!</h2>

            <p style="margin: 0 0 16px 0; color: #333333; font-size: 15px; line-height: 1.6; font-weight: 500;">
                Houve uma atualização nos nossos Termos de Uso e Política de Privacidade.
            </p>

            <p style="margin: 0 0 16px 0; color: #333333; font-size: 15px; line-height: 1.6;">
                Atualizamos os Termos de Uso e Política de Privacidade para explicar as ações do nosso sistema e oferecer mais informações. Os Termos e Política atualizados entram em vigor nesse momento para usuários existentes. Você pode ler o que mudou acessando Termos e Política na nossa tela inicial.
            </p>

            <p style="margin: 0 0 28px 0; color: #333333; font-size: 15px; line-height: 1.6;">
                Você não precisa fazer mais nada para concordar com os Termos e Política atualizados. Ao continuar usando o Morpheus Env, você aceita-os.
            </p>

            <p style="margin: 0 0 8px 0; color: #333333; font-size: 15px; font-weight: 500;">
                Agradecemos a compreensão! 🚀
            </p>

            <p style="margin: 0; color: #666666; font-size: 14px;">
                Equipe Morpheus Env, {date}
            </p>
        </div>

        <div style="background-color: #2d2d2d; padding: 30px 30px; border-left: 4px solid #7f22fe;">
            <h4 style="color: #ffffff; margin: 0 0 20px 0; font-size: 16px; font-weight: 600;">Morpheus Env</h4>

            <p style="color: #cccccc; font-size: 13px; line-height: 1.6; margin: 0 0 20px 0; text-align: center;">
                Esta mensagem foi enviada para <a href="mailto:{user_email}" style="color: #7f22fe; text-decoration: none;">{user_email}</a>.
                <br>
                Se tiver dúvidas ou reclamações, <a href="mailto:morpheusenv@gmail.com" style="color: #7f22fe; text-decoration: none; font-weight: 600;">fale conosco</a>.
            </p>

            <div style="margin: 0 0 20px 0; padding-top: 20px; border-top: 1px solid #444444; text-align: center;">
                <a href="https://eukauacavalcante.github.io/morpheus_env" style="color: #cccccc; text-decoration: none; font-size: 12px; font-weight: 600; margin-right: 8px;" target="_blank">Documentação</a>
                <span style="color: #666666; margin: 0 8px;">|</span>
                <a href="https://github.com/eukauacavalcante/morpheus_env" style="color: #cccccc; text-decoration: none; font-size: 12px; font-weight: 600; margin-left: 8px;" target="_blank">Github</a>
            </div>

            <p style="color: #999999; font-size: 12px; margin: 0 0 15px 0; text-align: center;">
                Morpheus Env | João Pessoa, Paraíba, Brasil
            </p>

            <div style="padding-top: 15px; border-top: 1px solid #444444; text-align: center;">
                <p style="color: #888888; font-size: 11px; margin: 0;">
                    © Morpheus Env - Projeto Acadêmico e Experimental
                </p>
            </div>
        </div>
    </div>
</body>
</html>
"""
