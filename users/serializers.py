from rest_framework import serializers
from .models import User
from rest_framework.response import Response

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=30,min_length=4)
    password=serializers.CharField(min_length=4)
    
    def validate(self, data):
        password=data.get('password')
        if not password.isdigit():
            raise serializers.ValidationError("Parol faqat raqamlardan iborat bo'lishi kerak")
        return data
        
class RegisterSerilizer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=['username','password','first_name','last_name','email']
    def validate(self, data):
        first_name=data.get('first_name')
        if len(first_name)<4 or len(first_name)>30:
            data={
                'messege':"First_name uzunligi 4 dan uzun 30 dn qisqa bo'lishi kerak "
            }
            return Response(data)
        last_name=data.get('last_name')
        if len(last_name)<4 or len(last_name)>30:
            data={
                'messege':"last_name uzunligi 4 dan uzun 30 dn qisqa bo'lishi kerak "
            }
            return Response(data)
        password=data.get('password')
        if not password.isdigit():
            return serializers.ValidationError("Parol faqat raqamlardan iborat bo'lishi kerak")
        return data
        
    def create(self, validated_data):
        user=User.objects.create_user(**validated_data)
        return user
        
     