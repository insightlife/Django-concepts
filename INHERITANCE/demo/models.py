from turtle import mode
from django.db import models

# Create your models here.
# Abstract inheritance
class team(models.Model):
    teamname= models.CharField(max_length=100)

    class Meta:
        abstract = True

class cricket(team):
    name = models.CharField(max_length=30)

# Multiple inheritance
class tool(models.Model):
    teamname= models.CharField(max_length=100)

class fooball(tool):
    name = models.CharField(max_length=30)

#proxy model inheritance
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
 
class MyPerson(Person):
    class Meta:
        proxy = True
 
    def fullName(self):
        return self.first_name + " " + self.last_name

class student(models.Model):
    firstname = models.CharField(max_length=80);
    lastname = models.CharField(max_length=60)

    def fullName(self):
        return self.firstname+" "+self.lastname