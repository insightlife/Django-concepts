from django import forms

class data(forms.Form):
    username=forms.CharField(max_length=40)
    password=forms.CharField(max_length=70)