from django import forms
from django.contrib.auth.models import User

from .models import Contact



class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name','number','company','email','image','is_favorite']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']



