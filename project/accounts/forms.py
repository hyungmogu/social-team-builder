from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from . import models

class SignUpForm(UserCreationForm):
    class Meta:
        model = models.User
        fields=('email', 'password1', 'password2', 'is_employer',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm'})

class SignInForm(AuthenticationForm):
    class Meta:
        model = models.User
        fields=('username', 'password',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Password'})
