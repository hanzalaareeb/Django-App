from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# Registeration from 

class RegisterationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text='Required. Add a valid email address')
    username = forms.CharField(max_length=255, help_text='Required. Add a valid username')
    password1 = forms.CharField(widget=forms.PasswordInput, help_text='Required. At least 8 characters long.')
    password2 = forms.CharField(widget=forms.PasswordInput, help_text='Required. Enter the same password as above, for verification')
    
    class Meta:
        model = get_user_model()
        fields = ('email','username', 'password1', 'password2')