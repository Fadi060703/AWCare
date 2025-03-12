from django.shortcuts import render
from django.contrib.auth import get_user_model 
from rest_framework import status , permissions 
from rest_framework.request import Request 
from rest_framework.response import Response 
from rest_framework.views import APIView 
from rest_framework.generics import ListCreateAPIView 
from rest_framework_simplejwt.views import TokenObtainPairView 
from .models import * 
from .serializers import * 

# Create your views here.

class UserRegisterView( ListCreateAPIView ) :
    queryset = get_user_model().objects.all() 
    serializer_class = UserSerializer 
    permission_classes = [ permissions.AllowAny ]
    
    def post( self , request : Request , *args , **kwargs ) :
        return super().post( request , *args , **kwargs )
    def perform_create(self, serializer):
        user = serializer.save( is_active=True )
        user.set_password( serializer.validated_data['password'] )
        user.save()
        
class DoctorRegisterView( ListCreateAPIView ) :
    queryset = Doctor.objects.all() 
    serializer_class = DoctorSerializer  
    permission_classes = [ permissions.AllowAny ]
    
    def post( self , request : Request , *args , **kwargs ) :
        return super().post( request , *args , **kwargs )
    def perform_create(self, serializer):
        user = serializer.save( is_active=True )
        user.set_password( serializer.validated_data['password'] )
        user.save()
    
class LoginView( TokenObtainPairView ) :
    serializer_class = EmailTokenObtainSerializer 