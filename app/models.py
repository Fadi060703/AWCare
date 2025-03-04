from django.db import models
from django.contrib.auth.models import AbstractUser , Group , Permission

# Create your models here.
class CustomUser( AbstractUser ) :   
    username = models.CharField( max_length = 20 , blank = False , unique = True ) 
    first_name = models.CharField( max_length = 30 , blank = False ) 
    last_name = models.CharField( max_length = 30 , blank = False ) 
    phone_number = models.CharField( max_length = 17 , blank = True )
    profile_image = models.ImageField( upload_to = 'profile_images/', null = True, blank = True )
    created_at = models.DateTimeField( auto_now_add = True )
    updated_at = models.DateTimeField( auto_now = True )
    groups = models.ManyToManyField( Group , related_name = "user_groups" , blank=True , null = True)
    user_permissions = models.ManyToManyField( Permission , related_name="customuser_user_permissions" , blank=True )
    