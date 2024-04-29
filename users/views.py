from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from .serializers import LoginSerializer,RegisterSerilizer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

class LoginView(APIView):
    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user=authenticate(username=serializer.data['username'],password=serializer.data['password'])

        if user is None:
            data={
                'status':'False',
                'messege':'User not found'
            }
            return Response(data)
        
        refrash=RefreshToken.for_user(user)
        data={
            'refrash':str(refrash),
            'access':str(refrash.access_token)
        }
        return Response(data)
    
class RegisterView(APIView):
    def post(self,request):
        serializer=RegisterSerilizer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)