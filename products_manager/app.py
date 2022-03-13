from flask import Flask, request, jsonify
from products_manager import ProductsManager
from db_conn import DBConn

app = Flask(__name__)

mysql = DBConn(app).make_conn()


@app.route('/products', methods=['GET'])
def get_products():
    response, status = ProductsManager(mysql).get_products()
    return jsonify(response), status


@app.route('/products', methods=['POST'])
def add_porduct():
    product = request.json
    response, status = ProductsManager(mysql).add_products(product['name'], product['amount'])
    return response, status


@app.route('/products', methods=['PUT'])
def order_product():
    product = request.json
    response, status = ProductsManager(mysql).order_products(product['name'], product['amount'])
    return response, status


if __name__ == '__main__':
    app.run()