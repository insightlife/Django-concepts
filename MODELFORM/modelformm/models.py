from django.db import models

class user(models.Model):
    name=models.TextField(max_length=10)
    email=models.TextField(max_length=60)
    password=models.TextField(max_length=80)