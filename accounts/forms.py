from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class signUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    usable_password = None

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')