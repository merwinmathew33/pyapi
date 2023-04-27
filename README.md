# pyapi
This is a simple web application for  user and order creation, retrieving details using user_id and order_id, built using flask, RESTful API and MongoDB
## Features
* Have separate table for orders and users in database which contains order_d, prodct name, quantity, total price and user_id, name, email_id, creation date respectively.
* Returns a list of users and orders present in that database
* Returns the details of a specific user and order using its unique id
## Installation
1. Clone the repository to your local machine.
2. Install the required dependencies.
    ```
   py -3 -m venv venv
    $ pip install Flask
    $ pip install Flask-PyMongo
  ```
3.  Run the python app.py to start the Flask web server.
  ```
  flask run --debug
  ```
 Now our program run in debug mode 
 
4. Open your web browser and go to http://localhost:5000 to access the application.
  
