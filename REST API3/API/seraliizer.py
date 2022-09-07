from .models import Student
from rest_framework import serializers

class studentSeralizier(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','roll','city']
