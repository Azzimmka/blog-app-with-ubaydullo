from cProfile import label

from django import forms
from .models import Articles
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import  User

class ArticlesForms(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ('title', 'description', 'image', 'category')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'border-red-500 rounded-2xl outline-none pl-[10px]',
                'placeholder': 'Enter title...'
            }),
            'description': forms.Textarea(attrs={
                'class': '.....'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': '....'
            }),
            'category': forms.Select(attrs={
                'class': '...'
            })
        }

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label = 'Name',
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your name...',
            'class': 'border border-red-500'
        })
    )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter your password...',
            'class': 'border border-red-500'
        })
    )


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label='Username',
        widget = forms.TextInput(attrs={
            'placeholder': 'Enter your username',
            'class': 'border border-red-600'
        })
    )

    first_name = forms.CharField(
        label = 'Name',
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your name',
            'class': 'border border-red-600'
        })
    )

    last_name = forms.CharField(
        label="Ваша фамилия",
        widget=forms.TextInput(attrs={
            "placeholder": "Введите фамилию...",
            "class": 'border border-red-600'
        })
    )

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            "placeholder": "Введите email...",
            "class": 'border border-red-600'
        })
    )

    password1 = forms.CharField(
        label='Password 1',
        widget=forms.PasswordInput(attrs={
            "placeholder": "Введите password...",
            "class": 'border border-red-600'
        })
    )

    password2 = forms.CharField(
        label='Password 2',
        widget=forms.PasswordInput(attrs={
            "placeholder": "Введите password 2...",
            "class": 'border border-red-600'
        })
    )

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")