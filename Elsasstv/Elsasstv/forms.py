from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    """This class, herited from UserCreationForm, allows for the creation of form objects used to register
    a new user.
    """
    username = forms.CharField(max_length=30, help_text='Required')
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, required=False, help_text='Optional')

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2', 
        )
        

class UserForm(forms.Form):
    """Class used for the authentification of users"""
    username = forms.CharField(max_length=40)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)

