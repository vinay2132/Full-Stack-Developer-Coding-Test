from flask import Flask, jsonify, request, abort, make_response
from threading import Lock

app = Flask(__name__)

products = [
    {'id': 1, 'product_name': 'Laptop', 'product_cost': 1200, 'product_value': 10},
    {'id': 2, 'product_name': 'Phone', 'product_cost': 800, 'product_value': 15},
]

lock = Lock()

def find_product(product_id):
    return next((product for product in products if product['id'] == product_id), None)

def error_response(message, status_code):
    return make_response(jsonify({'error': message}), status_code)


@app.route('/products', methods=['GET'])
def get_products():
    with lock:
        return jsonify({'products': products}), 200

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    with lock:
        product = find_product(product_id)
        if product is None:
            return error_response("Product not found", 404)
        return jsonify({'product': product}), 200

@app.route('/products', methods=['POST'])
def add_product():
    if not request.json or not 'product_name' in request.json:
        return error_response("Invalid data. Product must have a Product Name.", 400)
    
    with lock:
        new_product = {
            'id': products[-1]['id'] + 1 if products else 1,  # Auto-increment ID
            'product_name': request.json['product_name'],
            'product_cost': request.json.get('product_cost', 0),
            'product_value': request.json.get('product_value', 1)
        }
        products.append(new_product)
    
    return jsonify({'product': new_product}), 201  # 201: Created


@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    if not request.json:
        return error_response("Invalid data. No JSON payload provided.", 400)
    
    with lock:
        product = find_product(product_id)
        if product is None:
            return error_response("Product not found", 404)

        product['product_name'] = request.json.get('product_name', product['product_name'])
        product['product_cost'] = request.json.get('product_cost', product['product_cost'])
        product['product_value'] = request.json.get('product_value', product['product_value'])
    
    return jsonify({'product': product}), 200

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    with lock:
        product = find_product(product_id)
        if product is None:
            return error_response("Product not found", 404)
        
        products.remove(product)
    
    return jsonify({'message': 'Product deleted successfully'}), 204  # 204: No Content


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404


@app.route('/')
def hello_world():
    return 'Hi add /products to get all the list of products'


if __name__ == '__main__':
    app.run(debug=True)
