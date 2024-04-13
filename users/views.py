from rest_framework.exceptions import ValidationError
from django.shortcuts import render
from rest_framework import generics,status
from users.serializers import *
from users.models import CustomUser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q


# Create your views here.

class RegisterUserAPIView(generics.CreateAPIView):
    serializer_class = UserSerializers
    
    
    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        username = request.data.get('username')
        if CustomUser.objects.filter(email=email).exists():
            return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
        if CustomUser.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

        response = super().create(request, *args, **kwargs)
        return Response({
            'data': response.data,
            'message': 'Account created successfully'
        }, status=status.HTTP_201_CREATED)
        
        
class LoginAPIView(generics.CreateAPIView):
    serializer_class= LoginSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data = request.data, context={'request': request}
        )
        serializer.is_valid(raise_exception = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class GroupCreateAPIView(generics.ListCreateAPIView):
    queryset = Groups.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        query_data= super().get_queryset()
        group_id = self.request.data.get('group_id')
        if group_id is not None:
            query_data = query_data.filter(id=group_id)
            # return query_data
        
        return query_data
    
    def perform_create(self, serializer):
        owner = self.request.user

        # Add the owner as a member before saving
        group = serializer.save(Owner=owner)
        group.members.add(owner)

class UpdateGroupAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Groups.objects.all()
    serializer_class = GroupSerializer
    
    def patch(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            data = request.data
            
            if instance.Owner != request.user:
                return Response({"error": "You are not the owner of this group"}, status=status.HTTP_403_FORBIDDEN)
            
            if 'add_members' in data:
                members_to_add = data['add_members']
                for member in members_to_add:
                    member_id = CustomUser.objects.get(id=member)
                    instance.members.add(member_id)
            if 'remove_members' in data:
                members_to_rmv = data['remove_members']
                for member in members_to_rmv:
                    member_id = CustomUser.objects.get(id=member)
                    instance.members.remove(member_id)
        except ValueError:
            raise ValidationError("Invalid ID")
                
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CreateFolderAPIView(generics.ListCreateAPIView):
    permission_classes =[ IsAuthenticated ]
    serializer_class = FolderSerializer
    queryset = Folder.objects.all()
    
    
    
    def get_parent_folder(self):
        parent_folder_id = self.request.data.get('folder_id')
        if parent_folder_id is not None:
            return Folder.objects.filter(pk=parent_folder_id).first()
        return None
    
    def create(self, request, *args, **kwargs):
        parent_folder = self.get_parent_folder()
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        serializer.validated_data['parent_folder'] = parent_folder
        
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

class ManageFolderAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FolderSerializer
    queryset = Folder.objects.all()
    lookup_field = 'pk'
    


class CreateFilesAPIView(generics.ListCreateAPIView):
    permission_classes = [ IsAuthenticated ]
    serializer_class = FileSerializer
    queryset = File.objects.all()
    
    def get_queryset(self):
        querydata = super().get_queryset()
        folder_id = self.request.data.get('folder_id')
        if folder_id is not None:
            folder_data = querydata.filter(folder= folder_id)
        return folder_data
    
    

class ManageFilesAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FileSerializer
    queryset = File.objects.all()
    lookup_field = 'pk'


class FolderDataAPIView(generics.ListAPIView):
    serializer_class = FolderSerializer

    def get_queryset(self):
        folder_id = self.kwargs.get('folder_id')
        if folder_id:
            return Folder.objects.filter(id=folder_id)
        else:
            return Folder.objects.filter(parent_folder=None)

    def get(self, request, *args, **kwargs):
        folder_id = self.kwargs.get('folder_id')
        if folder_id:
            queryset = self.get_queryset()
            if queryset.exists():
                data = self.get_data(queryset)
                return Response(data)
            else:
                return Response({"message": "Folder not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            queryset = self.get_queryset()
            data = self.get_data(queryset)
            return Response(data)

    def get_data(self, queryset):
        data = []
        for folder in queryset:
            folder_data = {
                'id': folder.id,
                'name': folder.name,
                'sub_folders': [],
                'files': []
            }
            # Get subfolders recursively
            sub_folders = Folder.objects.filter(parent_folder=folder)
            folder_data['sub_folders'] = self.get_data(sub_folders)
            # Get files in current folder
            files = File.objects.filter(folder=folder)
            file_serializer = FileSerializer(files, many=True)
            folder_data['files'] = file_serializer.data
            data.append(folder_data)
        return data
    
class listusers(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = listSerializer
    
    
        