import importlib.resources

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

CSS_INPUT_CLASS = 'bg-white/10 border border-white/20 p-3 rounded-2xl text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent transition'


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': CSS_INPUT_CLASS})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': CSS_INPUT_CLASS,
                'placeholder': 'Pelo menos 8 caracteres.'
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': CSS_INPUT_CLASS})
    )

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': CSS_INPUT_CLASS,
                'placeholder': 'Letras, números e @/./+/-/_ apenas.',
            }),
            'email': forms.EmailInput(attrs={
                'class': CSS_INPUT_CLASS,
                'placeholder': 'Ex: usuario@email.com',
            })
        }

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        return first_name.title()

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('Esse usuário já existe')
        if username.isdecimal():
            raise ValidationError('Não é permitido apenas números')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        domain = email.split('@')[1].lower()
        with importlib.resources.open_text('users.validators', 'disposable_email_blocklist.conf') as f:
            blocklist_content = {line.strip().lower() for line in f if line.strip()}
        if domain in blocklist_content:
            raise ValidationError('E-mails temporários não são permitidos.')
        return email
