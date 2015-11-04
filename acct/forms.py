from django import forms
from django.core.exceptions import ValidationError

from acct.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=200, required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput(), max_length=200, required=True)
    remember_me = forms.BooleanField(label='Remember Me')

class PostForm(forms.Form):
    title = forms.CharField(required=True)


