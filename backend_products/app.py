from flask import Flask, request, make_response
from flask_cors import CORS
from routes.products_router import ProductRouter

product_router = ProductRouter()
app = Flask(__name__)
CORS(app)


@app.route("/products/<user>", methods=['GET'])
def get_products(user):
  response = make_response(product_router.list(user))
  response.headers.add("Access-Control-Allow-Origin", "*")
  response.headers.add("Access-Control-Allow-Headers", "*")
  response.headers.add("Access-Control-Allow-Methods", "*")
  return response

@app.route("/products/<user>", methods=['POST'])
def post_products(user):
  product_router.add(user, request.json['products'])
  return {}, 200

@app.route("/products/<user>", methods=['DELETE'])
def delete_products(user):
  product_router.remove(user, request.json['products'])
  return {}, 200

@app.route("/recipe/<user>", methods=['GET'])
def recipe(user):
  return product_router.search(user)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return {}, 404

if __name__ == "__main__":
    app.run(debug=True)