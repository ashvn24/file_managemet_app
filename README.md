
# File Management App

This project is a file management application designed to manage members, folders, and files. It consists of two user groups: owners and staff members. Users are authenticated using JSON Web Tokens (JWT) and have access to various API endpoints for managing users, groups, folders, and files.






## Installation
To run the project, follow these steps:

Clone the repository to your local machine.

Navigate to the project directory.

Run the following command to build and start the Docker containers for the first time:

Install my-project with npm

```
  docker-compose up --build
```
After the initial setup, you can simply use the following command to start the project:
```
  docker-compose up 
```

## Tech Stack

**Client:** Postman API

**Server:** Django, Django REST


## Features

- User Authentication: Users are authenticated using JWT. Signals are utilized to create user profiles upon registration.

- Custom Middleware: A custom middleware intercepts access tokens to check their expiry and obtains a new access token using the refresh token if needed.
- Dockerized Deployment: The project is dockerized, allowing for easy deployment and scalability. Docker containers encapsulate the application and its dependencies, ensuring consistency across different environments.


## API end points

```
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

```


## Authors

- [@Ashwin vk](https://github.com/ashvn24)

