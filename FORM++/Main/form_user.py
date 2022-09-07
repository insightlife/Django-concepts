from django import forms

from django.core import validators

def start_with_s(value):
    if value[0]!='s':
        raise forms.ValidationError

class user(forms.Form):
    name=forms.CharField(validators=[validators.MaxLengthValidator(10)])
    email=forms.CharField(widget=forms.EmailInput())
    password=forms.CharField(validators=[start_with_s])

    
    

      
    