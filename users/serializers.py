from rest_framework import serializers
from users.models import *
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'dateJoined']
        extra_kwargs ={
            'password':{'write_only': True},
            'dateJoined': {'read_only': True}
        }
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model( **validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    access_token = serializers.CharField(read_only=True)  # Field to store the token generated by Django Rest Framework JWT
    refresh_token = serializers.CharField(read_only=True)
    
    class  Meta: 
        model = CustomUser
        fields = ['email', 'password', 'access_token', 'refresh_token']
        
    def validate(self, data):
        email = data.get( 'email')
        password = data.get('password')
        request = self.context.get('request')
        user = authenticate(request, email=email, password=password)
        if not user:
            raise AuthenticationFailed('Invalid Email or Password')
        user_token = user.get_token()
        return{
            'email':user.email,
            'access_token': str(user_token.get('access')),
            'refresh_token':str(user_token.get('refresh'))
        }

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'phone_number', 'address']
class GroupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Groups
        fields = ['id', 'GroupName', 'Owner', 'members']
        extra_kwargs = {
            'Owner': {'read_only': True},  # Owner field should be read-only
            'members': {'required': False},  # members field is optional
            
        }
        
class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = ["id", "name", "parent_folder"]
        extra_kwargs = {
            'parent_folder': {"required":False}
        }

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields =["id", "name", "file", "folder"]
        

class listSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields ='__all__'