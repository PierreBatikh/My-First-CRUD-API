# My-First-CRUD-API(Flask)

A small learning project that implements a simple REST API using Flask. The API stores data in a local JSON file containing an array of objects, each with a **name** and **birthday**, and exposes CRUD operations to manage them. It’s designed as a beginner-friendly introduction to building APIs and handling basic data persistence without a database.

## Features
- Flask-based API with clear routing
- JSON-file storage instead of a database
- Create, read, update, and delete operations
- Lightweight structure suitable for learning and experimentation

## Endpoints
- **GET** `/all` — retrieve all stored birthdays
- **GET** `/today` — retrieve all stored birthdays on the day the API is fetched
- **GET** `/month` — retrieve all stored birthdays during the month when the API is fetched
- **POST** `/add` — add a new person  
- **PUT** `/update/<name>` — update an existing person’s data  
- **DELETE** `/remove/<name>` — remove a person by name  

## Learning Source
This tutorial is a good place to start your API journey:  
Tutoria[https://youtu.be/Ha3ls0EAtW8?si=epnBx1GJcW_fv_ut] 

## License
This project is for learning purposes only and is not licensed for production use.

