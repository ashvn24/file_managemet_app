File Management App
This project is a file management application designed to manage members, folders, and files. It consists of two user groups: owners and staff members. Users are authenticated using JSON Web Tokens (JWT) and have access to various API endpoints for managing users, groups, folders, and files.

Running the Project
To run the project, follow these steps:

Clone the repository to your local machine.

Navigate to the project directory.

Run the following command to build and start the Docker containers for the first time:
docker-compose up --build

After the initial setup, you can simply use the following command to start the project:
docker-compose up

Project Features
User Authentication: Users are authenticated using JWT. Signals are utilized to create user profiles upon registration.

Custom Middleware: A custom middleware intercepts access tokens to check their expiry and obtains a new access token using the refresh token if needed.

API Endpoints: The application provides various API endpoints for user management, group management, folder management, and file management.

Dockerized Deployment: The project is dockerized, allowing for easy deployment and scalability. Docker containers encapsulate the application and its dependencies, ensuring consistency across different environments.

API Endpoints
Register: http://127.0.0.1:8000/user/register/
Login: http://127.0.0.1:8000/user/login/
List Users: http://127.0.0.1:8000/user/list/
Manage User (by ID): http://127.0.0.1:8000/user/manageUser/<int:pk>/
Create Group: http://127.0.0.1:8000/user/group/
Update Group (by ID): http://127.0.0.1:8000/user/update/<int:pk>/
Add Folder: http://127.0.0.1:8000/user/addFolder/
Manage Folder (by ID): http://127.0.0.1:8000/user/manageFolder/<int:pk>/
Create Files: http://127.0.0.1:8000/user/file/
Manage Files (by ID): http://127.0.0.1:8000/user/manageFiles/<int:pk>/
List All (with Folder ID): http://127.0.0.1:8000/user/listAll/<int:folder_id>/
List All (without Folder ID): http://127.0.0.1:8000/user/listAll/

Feel free to explore these endpoints and their functionalities using your preferred API testing tool, such as Postman.

For any further questions or assistance, please reach out!
