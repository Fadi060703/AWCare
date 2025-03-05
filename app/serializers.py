from .models import * 
from rest_framework import serializers 
from django.contrib.auth import get_user_model 

class GroupSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = Group 
        fields = [ 'id' , 'name' ] 

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
                  'last_name' , 'email', 'password' ,
                  'phone_number', 'profile_image', 'group_ids','groups' ]
        
    def create(self, validated_data):
        group_ids = validated_data.pop( 'groups', [] )   
        user = get_user_model().objects.create( **validated_data )
        user.groups.set( group_ids )  
        return user