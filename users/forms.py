from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class_string = 'bg-white/10 border border-white/20 p-3 rounded-2xl text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent transition'


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': class_string})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': class_string,
                'placeholder': 'Pelo menos 8 caracteres.'
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': class_string})
    )

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': class_string,
                'placeholder': 'Letras, números e @/./+/-/_ apenas.',
            }),
            'email': forms.EmailInput(attrs={
                'class': class_string,
                'placeholder': 'Ex: usuario@email.com',
            })
        }

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        return first_name.title()

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username.isdecimal():
            raise ValidationError('Não é permitido apenas números')
        return username
