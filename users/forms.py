import importlib.resources

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

CSS_INPUT_CLASS = 'input-global'


def validate_first_name(first_name):
    return first_name.title()


def validate_username(username, instance=None):
    instance_id = instance.pk if instance else None
    if User.objects.filter(username=username).exclude(pk=instance_id).exists():
        raise ValidationError('Esse usuário já existe')
    if username.isdecimal():
        raise ValidationError('Não é permitido apenas números')
    return username


def validate_email(email):
    if email:
        domain = email.split('@')[1].lower()
        with importlib.resources.open_text('users.validators', 'disposable_email_blocklist.conf') as f:
            blocklist_content = {line.strip().lower() for line in f if line.strip()}
        if domain in blocklist_content:
            raise ValidationError('E-mails temporários não são permitidos.')
    return email


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': CSS_INPUT_CLASS}),
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': CSS_INPUT_CLASS,
                'placeholder': 'Pelo menos 8 caracteres.',
            }
        )
    )
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': CSS_INPUT_CLASS}))

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': CSS_INPUT_CLASS,
                    'placeholder': 'Letras, números e @/./+/-/_ apenas.',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': CSS_INPUT_CLASS,
                    'placeholder': 'Ex: usuario@email.com',
                }
            ),
        }

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        return validate_first_name(first_name=first_name)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        return validate_username(username=username, instance=self.instance)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return validate_email(email=email)


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': CSS_INPUT_CLASS,
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': CSS_INPUT_CLASS,
                    'placeholder': 'Letras, números e @/./+/-/_ apenas.',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': CSS_INPUT_CLASS,
                    'placeholder': 'Ex: usuario@email.com',
                }
            ),
        }

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        return validate_first_name(first_name=first_name)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        return validate_username(username=username, instance=self.instance)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return validate_email(email=email)
