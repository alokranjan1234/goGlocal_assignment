
# GoGlocal Assignment

A Django application for authenticating users using JWT tokens

## Task list
1. Base django app
2. User login model (extend User)
3. setup django admin superuser
4. create base user using admin panel
5. login endpoint that takes user login and returns JWT token
6. profile endpoint that takes JWT returns users first_name, last_name
7. middleware for jwt_authentication
8. update profile endpoint to return request.user

## Endpoints
    ### login
    ```curl -X POST   -H "Content-Type: application/json"   -d '{"username": "test_user", "password": "test#123$"}'   http://localhost:8000/auth/api/user/login/```

    ### profile info
    ```curl -X GET  http://localhost:8000/auth/api/user/profile/ -H 'Authorization: Token {ACCESS_TOKEN}'``