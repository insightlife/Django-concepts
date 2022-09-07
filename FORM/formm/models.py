from django.db import models

class student_no(models.Model):
    id=models.CharField(max_length=64,primary_key=True)
    email=models.EmailField(default='test@gmail.com')


