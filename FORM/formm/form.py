from django import forms

def check(value):
    if value[0] == 'z':
        raise forms.ValidationError("string should not start with z")

class student(forms.Form):
    name=forms.CharField(validators=[check])
    email=forms.EmailField()
    text=forms.CharField()
    def clean(self):
        all_cleandata=super().clean()
        email=all_cleandata['email']
        if email=='suman@123.com':
            print("you are super user")
        else:
            print("you are normal user")