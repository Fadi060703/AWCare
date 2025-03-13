from .models import * 
from rest_framework import serializers 
from django.contrib.auth import get_user_model  
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 

User = get_user_model()

class GroupSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = Group 
        fields = [ 'id' , 'name' ] 

class EmailTokenObtainSerializer( TokenObtainPairSerializer ) :
    username_field = User.USERNAME_FIELD  
    
    def validate(self, attrs):
        data = super().validate(attrs)
        data['email'] = self.user.email
        data['user_id'] = self.user.id
        return data   

class CustomTokenObtainPairView(TokenObtainPairSerializer):
    def validate(self, attrs):
        try:
            attrs['username'] = attrs.get('email', '')
            return super().validate(attrs)
        except User.DoesNotExist:
            raise serializers.ValidationError('Invalid credentials')

class UserSerializer( serializers.ModelSerializer ) :
    password = serializers.CharField( write_only = True )
    groups = GroupSerializer(many=True, read_only=True) 
    group_ids = serializers.PrimaryKeyRelatedField(
        write_only=True,
        many=True,
        required=False,
        queryset=Group.objects.all(),
        source='groups'
    )
        
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'first_name' ,
                  'last_name' , 'email', 'gender' , 'password' ,
                  'phone_number' , 'profile_image', 'group_ids','groups' ]
        
    def create(self, validated_data):
        group_ids = validated_data.pop( 'groups', [] )   
        user = get_user_model().objects.create( **validated_data )
        user.groups.set( group_ids )  
        return user
    
class SpecializationSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = Speicalization 
        fields = [ 'specialization' ] 
    
class NationalitySerializer( serializers.ModelSerializer ) :
    class Meta :
        model = Nationality 
        fields = [ 'country' ] 

class LanguageSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = Language
        fields = [ 'name' ]
    
class DoctorProfileSerializer( serializers.ModelSerializer ) :
    nationalities = NationalitySerializer( read_only = True ) 
    languages = LanguageSerializer( read_only = True ) 
    speicalization = SpecializationSerializer( read_only = True )
    class Meta :
        model = DoctorProfile 
        fields = [ 'doc' , 'specialization' , 'sign' , 'service_type' , 'about_me' , 'nationalities' , 'languages' ] 
        
