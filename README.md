## E-Shop
A simple API for creating and buying various products

## Getting started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Prerequisites
This is a project written using Python, Django and Django Rest Framework

**1.** Clone the repository
https://github.com/kimmmka/task4.git

**2.** Install the requirements

```sh
*pip install -r requirements.txt* 
```

**3.**Go to the project through the console window and enter: 
```sh
docker-compose up --build -d

```

**4.** Open a console window in Docker and make migrations
```sh
 *python manage.py makemigrations*

 *python manage.py migrate*
```

**5.** Create a new superuser

##### *python manage.py createsuperuser*

**6.**Server started
go to: [site](http://127.0.0.1:8000/admin/course)

## Built With

Django - The framework used, Django Rest Framework - The toolkit used to build API, Swagger UI - for API documentation.

## Documentation
