from django.db import models
from django.contrib.auth.models import BaseUserManager , AbstractUser , Group , Permission , PermissionsMixin

# Create your models here.

class CustomUserManager( BaseUserManager ) :
    def create_user(self, email , password = None , **extra_fields ):
        if not email:
            raise ValueError( 'The Email field must be set' )
        email = self.normalize_email( email )
        user = self.model( email = email , **extra_fields )
        user.set_password( password )
        user.save( using = self._db )
        return user
    
    def create_superuser( self , email , password = None , **extra_fields ):
        extra_fields.setdefault( 'is_staff' , True )
        extra_fields.setdefault( 'is_superuser' , True )

        return self.create_user( email , password , **extra_fields )
    
class CustomUser( AbstractUser , PermissionsMixin ) :   
    username = models.CharField( max_length = 20 , blank = False , unique = True ) 
    email = models.EmailField( unique = True ) 
    first_name = models.CharField( max_length = 30 , blank = False ) 
    last_name = models.CharField( max_length = 30 , blank = False ) 
    phone_number = models.CharField( max_length = 17 , blank = True )
    profile_image = models.ImageField( upload_to = 'profile_images/', null = True, blank = True )
    created_at = models.DateTimeField( auto_now_add = True )
    updated_at = models.DateTimeField( auto_now = True )
    groups = models.ManyToManyField( Group , related_name = "user_groups" , blank=True , null = True)
    user_permissions = models.ManyToManyField( Permission , related_name="customuser_user_permissions" , blank=True )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 
    objects = CustomUserManager()
    
    def get_by_natural_key( self , email ) :
        return self.get( email = email )
