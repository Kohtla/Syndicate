from django.contrib.auth.models import User
from django import forms
from .models import Message

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    class Meta:
        model = User
        fields =  ['username', 'email','password']

class LoginUserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}))

class SendMessageForm(forms.ModelForm):
    message_text = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control"}))
    class Meta:
        model = Message
        fields = ['message_text']


