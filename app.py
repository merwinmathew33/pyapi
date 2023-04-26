from flask import Flask,render_template, jsonify, request, redirect
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

@app.route('/get_user_details', methods=['GET', 'POST'])
def get_user_details():
    if request.method == 'POST':
        user_id = request.form['user_id']
        return redirect('/users/'+user_id)
    else:
        return render_template('getu.html')


@app.route('/users/<string:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    # Get a specific user by id from the users collection
    user = users_collection.find_one({'id': user_id}, {'id': 0})
    if user is None:
        return render_template('user_details.html', user=None)
    else:
        return render_template('user_details.html', user=user)



@app.route('/get_order_details', methods=['GET', 'POST'])
def get_order_details():
    if request.method == 'POST':
        order_id = request.form['order_id']
        return redirect('/porders/'+order_id)
    else:
        return render_template('geto.html')


@app.route('/orders', methods=['GET'])
def get_all_orders():
    # Get all orders from the orders collection
    orders = list(orders_collection.find())
    return render_template('orders.html', orders=orders)

@app.route('/porders/<string:order_id>', methods=['GET'])
def get_order_by_id(order_id):
    # Get a specific order by id from the orders collection
    order = orders_collection.find_one({'id': order_id}, {'_id': 0})
    if order is None:
        return jsonify({'error': 'Order not found'}), 404
    return render_template('order_details.html', order=order)


@app.route('/ausers', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        # Add a new user to the users collection
        user_data = {
            'id': request.form['id'],
            'name': request.form['name'],
            'email': request.form['email'],
            'created_at': datetime.now()
        }
        result = users_collection.insert_one(user_data)
        return render_template('index.html')
    else:
        return render_template('add_users.html')

@app.route('/aorders', methods=['POST','GET'])
def add_order():
    if request.method == 'POST':
        # Add a new order to the orders collection
        order_data = {
            'id': request.form['id'],
            'user_id': request.form['user_id'],
            'product_name': request.form['product_name'],
            'quantity': request.form['quantity'],
            'total_price': request.form['total_price'],
            'created_at': datetime.now()
        }
        result = orders_collection.insert_one(order_data)
        return render_template('index.html')
    else:
        return render_template('add_orders.html')
    
if __name__ == '__main__':
    app.run(debug=True)
