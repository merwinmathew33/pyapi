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


## How to use
![image](https://user-images.githubusercontent.com/95087459/234883408-c4f5fe51-1e34-49a2-a805-b5c2c738de0f.png)

* Returns a list of all users in the system.
* Returns the details of a specific user.
* Returns a list of all orders in the system.
* Returns the details of a specific order.
* Add user into database
* Add order into database
