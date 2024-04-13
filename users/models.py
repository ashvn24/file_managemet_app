from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group
from .manager import UserManager
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone


# Create your models here.


class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique = True)
    username = models.CharField(max_length = 100)
    dateJoined = models.DateTimeField(default=timezone.now, editable=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELD = []
    
    objects = UserManager()
    
    def __str__(self):
        return self.email
    
    def get_token(self):
        refresh = RefreshToken.for_user(self)
        
        return{
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        
class UserProfile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s profile"
    
class Groups(models.Model):
    GroupName = models.CharField(max_length=50)
    Owner = models.ForeignKey(CustomUser, related_name='group_owner', on_delete=models.CASCADE)
    members = models.ManyToManyField(CustomUser, related_name='group_members')
    
    def __str__(self):
        return f'{self.Owner.username}"s group-{self.GroupName}'
    
class Folder(models.Model):
    name = models.CharField(max_length=100, null=False)
    parent_folder = models.ForeignKey('self', on_delete=models.CASCADE, null =True, blank=True)
    
    def __str__(self):
        if self.parent_folder is not None:
            return f'{self.name}/{self.parent_folder}'
        else:
            return self.name

class File(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to="files/")
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    
    def __str__(self):
        return  f'{self.name} in {self.folder.name}-folder'
    

    
    
