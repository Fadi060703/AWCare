from django.shortcuts import render
from rest_framework import status , permissions 
from rest_framework.request import Request 
from rest_framework.response import Response 
from rest_framework.views import APIView 
from rest_framework.generics import ListCreateAPIView 
from .models import * 
from .serializers import * 

# Create your views here.

class RegisterView( ListCreateAPIView ) :
    queryset = get_user_model().objects.all() 
    serializer_class = UserSerializer 
    permission_classes = [ permissions.AllowAny ]
    
    def post( self , request : Request , *args , **kwargs ) :
        return super().post( request , *args , **kwargs )
    