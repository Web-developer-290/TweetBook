from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Form(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
        
        
class UserRegister(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
        
class SearchForm(forms.Form):
    query = forms.CharField(label='Search Tweets', max_length=100, required=False)