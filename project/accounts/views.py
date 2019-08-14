from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import FormView, CreateView

from . import forms

class LoginView(FormView):
    form_class = forms.SignInForm
    success_url = reverse_lazy('profile')
    template_name = 'accounts/signin.html'

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(self.request, **self.get_form_kwargs())

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

class LogOutView(RedirectView):
    url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)

class SignUpView(CreateView):
    form_class = forms.SignUpForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'
