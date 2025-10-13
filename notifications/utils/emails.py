EMAIL_NEW_USER_TEXT = (
    'Olá, {user_first_name}! Obrigado por se cadastrar e utilizar o Morpheus Env.'
    ' Este projeto foi desenvolvido com fins experimentais e acadêmicos — voltado à pesquisa, aprendizado e demonstração de conceitos.'
    ' Por isso, pedimos que os resultados e recursos do sistema não sejam interpretados como serviços profissionais ou comerciais.'
    '\nPara conhecer mais sobre o projeto, acesse nosso repositório oficial: https://github.com/eukauacavalcante/morpheus_env'
    '\nCaso tenha sugestões de melhorias ou precise reportar algum problema, entre em contato conosco através do e-mail: morpheusenv@gmail.com'
    '\nEstamos felizes em tê-lo(a) conosco!'
    '\nEquipe Morpheus Env, {date}'
)

EMAIL_NEW_USER_HTML = """
    <html>
    <body style="font-family: Arial, sans-serif; line-height: 1.6; max-width: 600px; margin: 0 auto; padding: 20px;">
        <div style="background-color: #f8f9fa; border-radius: 8px; padding: 30px; border-left: 4px solid #4d179a;">
            <h2 style="color: #7f22fe; margin-top: 0;">Olá, {user_first_name}!</h2>
            <p style="margin-bottom: 15px;">
                Obrigado por se cadastrar e utilizar o <strong>Morpheus Env</strong>.
            </p>
            <p style="margin-bottom: 15px;">
                Este projeto foi desenvolvido com fins <strong>experimentais e acadêmicos</strong> — voltado à pesquisa, aprendizado e demonstração de conceitos. Por isso, pedimos que os resultados e recursos do sistema não sejam interpretados como serviços profissionais ou comerciais.
            </p>
            <div style="background-color: #ffffff; border-radius: 6px; padding: 20px; margin: 20px 0; border: 1px solid #e0e0e0;">
                <p style="margin-bottom: 10px; font-weight: bold; color: #8e51ff;">📚 Conheça mais sobre o projeto:</p>
                <p style="margin-bottom: 0;">
                    <a href="https://github.com/eukauacavalcante/morpheus_env"
                    style="color: #4a90e2; text-decoration: none; font-weight: 500;"
                    target="_blank">
                        https://github.com/eukauacavalcante/morpheus_env
                    </a>
                </p>
            </div>
            <div style="background-color: #ffffff; border-radius: 6px; padding: 20px; margin: 20px 0; border: 1px solid #e0e0e0;">
                <p style="margin-bottom: 10px; font-weight: bold; color: #8e51ff;">💬 Sugestões ou problemas?</p>
                <p style="margin-bottom: 0;">
                    Entre em contato conosco através do e-mail:
                    <a href="mailto:morpheusenv@gmail.com"
                    style="color: #4a90e2; text-decoration: none; font-weight: 500;">
                        morpheusenv@gmail.com
                    </a>
                </p>
            </div>
            <p style="margin-bottom: 0; margin-top: 25px; font-weight: 500;">
                Estamos felizes em tê-lo(a) conosco! 🚀
            </p>
            <p style="margin-bottom: 0; margin-top: 5px; font-weight: 500;">
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

EMAIL_TERMS_UPDATED = """
    <html>
    <body style="font-family: Arial, sans-serif; line-height: 1.6; max-width: 600px; margin: 0 auto; padding: 20px;">
        <div style="background-color: #f8f9fa; border-radius: 8px; padding: 30px; border-left: 4px solid #4d179a;">
            <h2 style="color: #7f22fe; margin-top: 0;">Parabéns, {user_first_name}!</h2>
            <p style="margin-bottom: 15px;">
                Esse é um teste do <strong>Morpheus Env</strong> (e um presente à você...).
            </p>
            <p style="margin-bottom: 15px;">
                Estamos implementando um sistema de envio de e-mail para todos os usuários após haver mudanças nos Termos de Uso e na Política de Privacidade do nosso software. <strong>Escolhemos VOCÊ</strong> para ficar responsável pela criação de uma mensagem utilizando o contexto acima.
            </p>
            <p style="margin-bottom: 15px;">
                Você tem missão de criar uma mensagem avisando ao usuário sobre a mudança nos termos e na política. Calma, é bem simples! Já temos uma estrutura HTML e CSS base, sua responsabilidade é apenas o alerta ao usuário, {user_first_name} 😊.
            </p>
            <p style="margin-bottom: 15px;">
                Para mais informações, entre em contato com o setor de Desenvolvimento de Softwares (vulgo Kauã)
            </p>
            <p style="margin-bottom: 0; margin-top: 25px; font-weight: 500;">
                Agradecemos a compreensão! (e a paciência) 🚀
            </p>
            <p style="margin-bottom: 0; margin-top: 5px; font-weight: 500;">
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
