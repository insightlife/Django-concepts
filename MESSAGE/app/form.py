from .models import user

from django import forms


class user_form(forms.ModelForm):
    class Meta:
        model = user
        fields=['name','password']