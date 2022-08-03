# docker-container-flask-API
The propuse is work with docker populate database from Centos server and reques information from flask API

# Run commads
In the root folder run
```docker-compose build```
```docker-compose up```
This will initialize the container build process and start the services.  
Or run this commands if you want pgadmin and volumn to work with you API in debug mode
```docker-compose -f docker-compose-dev.yml build```
```docker-compose -f docker-compose-dev.yml up```


# Endpoints
To make requests there are four endpoints in the API

1. ```localhost:5000/read```
returns the complete list of employees or users
2. ```localhost:5000/delete/<id>```
Delete user with id
3. ```localhost:5000/create```
Create a new employee, with post method you can use this template to post new data
```
{
    "first_name":"Juan", 
    "last_name":"Ramirez", 
    "phone1":"33246895", 
    "phone2":"33246895",
     "email":"roadriogoMontes@gmail.com",
    "streetAddress":"lopez mateos", 
    "zip_code":"44351",
     "city":"GDL", 
     "state":"Jalisco", 
     "company":"GdlCompany",
     "departaments":["Ventas"]
}
```

4. ```localhost:5000/```
returns welcom to API

# Branchs
There are two branch "development"  and "main". 
The development branch is used to create new features or solve bugs and test API.
The main API is where the code is tested and API works correctly


It is recommended to use POSTMAN or a similar service to be able to make the requests




# Database E-R diagram
![Diagrama en blanco (1)](https://user-images.githubusercontent.com/7892358/182441975-eb238b48-919e-42e5-bf4f-bb0d6f9ae825.png)
