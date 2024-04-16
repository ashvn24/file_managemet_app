
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



## Authors

- [@Ashwin vk](https://github.com/ashvn24)

