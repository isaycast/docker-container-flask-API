# docker-container-flask-API
The propuse is work with docker populate database from Centos server and reques information from flask API

# Run commads
In the root folder run
```docker-compose build```
```docker-compose up```
This will initialize the container build process and start the services

# Endpoints
To make requests there are three endpoints in the API

1. ```localhost:5000/read```
returns the complete list of employees or users
2. ```localhost:5000/delete/<id>```
Delete user with id
3. ```localhost:5000/```
returns welcom to API

# Branchs
There are two branch "development"  and "main". The development branch contains an extra pgAdmin wrapper that helps visualize data inserted into tables, it is located at port: 5050

The main branch contains only port 5000 to be able to make requests to the API

It is recommended to use POSTMAN or a similar service to be able to make the requests


# Database E-R diagram
![Diagrama en blanco (1)](https://user-images.githubusercontent.com/7892358/182441975-eb238b48-919e-42e5-bf4f-bb0d6f9ae825.png)
