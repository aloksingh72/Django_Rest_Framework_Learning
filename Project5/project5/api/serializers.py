from rest_framework import serializers
from .models  import Student


# priority of validations
# Validators function > Field-level validation > Object-level validation
#validators function for validation

def starts_with_r(value):
    if value[0].lower()!= 'r':
        raise serializers.ValidationError('Name should start with R')

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length =100,validators = [starts_with_r])
    rollno = serializers.IntegerField()
    city = serializers.CharField(max_length =100)

    def create(self,validated_data):
        return Student.objects.create(**validated_data)
    def update(self,instance,validated_data):
        print(instance.name)
        instance.name = validated_data.get('name',instance.name)
        print(instance.name)
        instance.rollno = validated_data.get('rollno',instance.rollno)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance
    
    #Field level validation
    def validate_rollno(self,value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value
    
    #object level validation
    def validate(self,data):
        nm  = data.get('name')
        ct = data.get('city')
        print(nm)
        print(ct)
        if nm.lower() == 'rohit' and ct.lower() != 'ranchi':
            raise serializers.ValidationError('city must ne ranchi')
        return data





