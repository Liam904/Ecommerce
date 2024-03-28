from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class LoginForm(AuthenticationForm):
      username= forms.CharField(widget=forms.TextInput(attrs=
    {
        'placeholder':"username",
        'class': 'w-full py-4 px-6 rounded-xp'
    }
    ))
      password = forms.CharField(widget=forms.PasswordInput(attrs=
    {
        'placeholder':"password",
        'class': 'w-full py-4 px-6 rounded-xp'
    }
    ))
    
    
    
      


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


    username= forms.CharField(widget=forms.TextInput(attrs=
    {
        'placeholder':"username",
        'class': 'w-full py-4 px-6 rounded-xp'
    }
    ))
    email= forms.CharField(widget=forms.EmailInput(attrs=
    {
        'placeholder':"email",
        'class': 'w-full py-4 px-6 rounded-xp'
    }
    ))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=
    {
        'placeholder':"password",
        'class': 'w-full py-4 px-6 rounded-xp'
    }
    ))
    
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=
    {
        'placeholder':"password",
        'class': 'w-full py-4 px-6 rounded-xp'
    }
    ))
    