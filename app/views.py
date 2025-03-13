from django.shortcuts import render
from django.contrib.auth import get_user_model 
from rest_framework import status , permissions 
from rest_framework.request import Request 
from rest_framework.response import Response 
from rest_framework.views import APIView 
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView 
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
        
class LoginView( TokenObtainPairView ) :
    serializer_class = EmailTokenObtainSerializer 
    
class SpecializationListCreateView( ListCreateAPIView ) :
    queryset = Speicalization.objects.all() 
    serializer_class = SpecializationSerializer 
    
class SpecializationDetailView( RetrieveUpdateDestroyAPIView ) :
    queryset = Speicalization.objects.all() 
    serializer_class = SpecializationSerializer 
    
class NationalityListCreateView( ListCreateAPIView ) :
    queryset = Nationality.objects.all() 
    serializer_class = NationalitySerializer 

class NationalityListDetailView( RetrieveUpdateDestroyAPIView ) :
    queryset = Nationality.objects.all() 
    serializer_class = NationalitySerializer

class ListCreateLanguageView( ListCreateAPIView ) :
    queryset = Language.objects.all() 
    serializer_class = LanguageSerializer 

class LanguageDetailView( RetrieveUpdateDestroyAPIView ) :
    queryset = Language.objects.all() 
    serializer_class = LanguageSerializer 
     