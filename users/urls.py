from django.urls import path
from users.views import *
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('token/refresh',TokenRefreshView.as_view(),name= 'token_refresh'),
    
    path('register/',RegisterUserAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('list/',listusers.as_view()),
    path('manageUser/<int:pk>/',UpdateUSer.as_view()),
    
    path('group/', GroupCreateAPIView.as_view()),
    path('update/<int:pk>/', UpdateGroupAPIView.as_view()),
    
    path('addFolder/', CreateFolderAPIView.as_view()),
    path('manageFolder/<int:pk>/', ManageFolderAPIView.as_view()),
    
    path('file/', CreateFilesAPIView.as_view()),
    path('manageFiles/<int:pk>/', ManageFilesAPIView.as_view()),
    
    path('listAll/<int:folder_id>/', FolderDataAPIView.as_view()),
    path('listAll/', FolderDataAPIView.as_view()),
    
]
