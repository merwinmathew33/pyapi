from flask import Flask,render_template, jsonify, request
from pymongo import MongoClient
from datetime import datetime

# Initialize the Flask app
app = Flask(__name__)

# Initialize the MongoDB client and database
client = MongoClient('mongodb://localhost:27017/')
db = client['pycray']

# Initialize the users and orders collections
users_collection = db['users']
orders_collection = db['orders']

@app.route("/")
def begin():
    return render_template('index.html')


# Define the API endpoints

@app.route('/users', methods=['GET'])
def get_all_users():
    # Get all users from the users collection
    users = list(users_collection.find({}, {'_id': 0}))
    return render_template('all_users.html', users=users)


@app.route('/users/<string:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    # Get a specific user by id from the users collection
    user = users_collection.find_one({'id': user_id}, {'_id': 0})
    if user is None:
        return render_template('user_details.html', user=None)
    else:
        return render_template('user_details.html', user=user)


@app.route('/orders', methods=['GET'])
def get_all_orders():
    # Get all orders from the orders collection
    orders = list(orders_collection.find({}, {'_id': 0}))
    return render_template('orders.html', orders=orders)

@app.route('/orders/<string:order_id>', methods=['GET'])
def get_order_by_id(order_id):
    # Get a specific order by id from the orders collection
    order = orders_collection.find_one({'id': order_id}, {'_id': 0})
    if order is None:
        return jsonify({'error': 'Order not found'}), 404
    return jsonify(order)

@app.route('/ausers', methods=['POST'])
def add_user():
    # Add a new user to the users collection
    user_data = request.get_json()
    user = {
        'id': user_data['id'],
        'name': user_data['name'],
        'email': user_data['email'],
        'created_at': datetime.now()
    }
    result = users_collection.insert_one(user)
    return jsonify({'message': 'User added successfully', 'id': str(result.inserted_id)})
@app.route('/orders', methods=['POST'])
def add_order():
    # Add a new order to the orders collection
    order_data = request.get_json()
    order = {
        'id': order_data['id'],
        'user_id': order_data['user_id'],
        'product_name': order_data['product_name'],
        'quantity': order_data['quantity'],
        'total_price': order_data['total_price'],
        'created_at': datetime.now()
    }
    result = orders_collection.insert_one(order)
    return jsonify({'message': 'Order added successfully', 'id': str(result.inserted_id)})
    
if __name__ == '__main__':
    app.run(debug=True)
