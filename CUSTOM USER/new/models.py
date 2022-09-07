from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User

# Create your models here.
class customuser(Model):
    user_name = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    slotdate = models.DateField(default='2022-07-02')
    slottime = models.DateTimeField()