from django import forms


class UserForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)