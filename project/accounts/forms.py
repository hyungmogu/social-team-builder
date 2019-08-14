from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={'placeholder':'Enter email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    class Meta:
        model = User
        fields=('email', 'password1', 'password2',)
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder':'Enter email'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})
        }
