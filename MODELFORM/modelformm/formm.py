from django import forms

from .models import user

class user_reg(forms.ModelForm):
    class Meta:
        model=user
        fields=['name','email','password']
        labels={'name':'enter your name','email':'enter your email','password':'enter your password'}
        widgets={'email':forms.EmailInput,'password':forms.PasswordInput}