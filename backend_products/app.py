from flask import Flask, request, jsonify
from routes.products_router import ProductRouter


product_router = ProductRouter()
app = Flask(__name__)

@app.route("/products/<user>", methods=['GET'])
def get_products(user):
  return jsonify(list(product_router.list(user)))

@app.route("/products/<user>", methods=['POST'])
def post_products(user):
  product_router.add(user, request.json['products'])
  return {}, 200

@app.route("/products/<user>", methods=['DELETE'])
def delete_products(user):
  product_router.remove(user, request.json['products'])
  return {}, 200


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return {}, 404


if __name__ == "__main__":
    app.run(debug=True)