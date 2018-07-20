# Example of Microservices in Python

## Overview
This is an example project which demonstrates the use of microservices for making offers.
Backend is powered by 2 microservices, all of which happen to be written in Python using Sanic.
* Users Service: Allows users to register and authenticate. Also provides information about users.
* Offers Service: Allows users to add offers to database and get information about them.

## Requirements
* Python 3.6
* Docker

## Docker

You can build project using the docker-compose file:
```
$ docker-compose up --build
```

Microservices Users and Offers will be running on the [localhost:8000](localhost:8000) and 
[localhost:8001](localhost:8001) respectively.<br> It also starts MongoDB running on the port 27017.

To stop run:
 ```
$ docker-compose stop
```
To remove images and services:
 ```
$ docker-compose down
```
You can also change environmental variables in docker-compose.yml

## Built With

* [Sanic](http://sanic.readthedocs.io/en/latest/) - Sanic is a 
Flask-like Python 3.5+ web server that’s written to go fast. It’s based on the work done by the amazing folks at 
magicstack.
 
* [Motor](hhttps://motor.readthedocs.io/en/stable/) - Motor presents a coroutine-based API for non-blocking access
 to MongoDB from Tornado or asyncio.
 
* [Sanic-JWT](https://sanic-jwt.readthedocs.io/en/latest/) - Sanic JWT adds authentication protection and endpoints
 to Sanic.

* [MongoDB](https://docs.mongodb.com/) - MongoDB is a document database with the scalability and flexibility that you 
want with the querying and indexing that you need.


## Authors

* **Anton Levakin** - *Initial work* - [Levakin](https://github.com/Levakin)

## License

This project is licensed under the Apachem 2.0 License - see the [LICENSE.md](LICENSE.md) file for details