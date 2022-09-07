from rest_framework import serializers
from .models import Student

class studentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=60)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=60)

    def create(self,validated_data):
        return Student.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.name= validated_data.get('name',instance.name)
        instance.roll= validated_data.get('roll',instance.roll)
        instance.city= validated_data.get('city',instance.city)
        instance.save()
        return instance

    def validate_roll(self,value):
        if value>200:
            raise serializers.ValidationError("seat full")
        return value

    def validate(self, data):
        nm=data.get('name')
        ct=data.get('city')
        if nm.lower() == 'rohit' and ct != 'ranchi':
            raise serializers.ValidationError('city must be ranchi')
        return data
        
