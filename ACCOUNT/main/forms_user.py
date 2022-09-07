from django.forms import forms

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class data(UserCreationForm):
    class Meta:
        model = User
        fields =['username','first_name','last_name','email']    


class data_up(UserChangeForm):
    password=None
    class Meta:
        model = User
        fields =['username','first_name','last_name','email','date_joined','last_login']    