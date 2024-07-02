from django import forms

from django.contrib.auth.forms import UserCreationForm

from userauths.models import User, Profile

class UserRegisterForm(UserCreationForm):
    full_name=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"enter your full names", 'class':'a custom class'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={"placeholder":"enter your email"}))
    username=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"enter your email"}))
    phone=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"enter your phone number"}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"enter your password"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Confirm your password"}))


    class Meta:
        model=User
        fields=['full_name','username','email','phone','password1','password2']