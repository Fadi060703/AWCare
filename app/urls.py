from django.urls import path 
from .views import * 
urlpatterns = [
    path( 'register/user' , UserRegisterView.as_view() , name = 'register-user' ) ,
    path( 'login' , LoginView.as_view() , name = 'login' ) , 
]
