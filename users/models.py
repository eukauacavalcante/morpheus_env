from django.db import models


class TermsOfUseAndPrivacyPolicy(models.Model):
    content = models.TextField(verbose_name='Conteúdo')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    is_active = models.BooleanField(default=True, verbose_name='Situação')

    class Meta:
        verbose_name = 'Termos de Uso e Política de Privacidade'

    def __str__(self):
        return f'Termos e Políticas atualizados em {self.updated_at}'
