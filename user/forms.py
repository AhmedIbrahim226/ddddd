from django import forms
from django.contrib.auth import authenticate, login , logout
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            user = authenticate(self.request, username=email, password=password)
            if user is not None:
                login(self.request, user)
            else:
                raise ValidationError('The entered data not valid, invalid credentials')