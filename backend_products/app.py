from flask import Flask, request, make_response
from flask_cors import CORS
from routes.products_router import ProductRouter

product_router = ProductRouter()
app = Flask(__name__)
CORS(app)


# Lazily run code, and add headers even if it fails.
def response_wrapper(data, code=200):
  try:
    response = make_response(data(), code)
  except:
    response = make_response({}, 500)

  response.headers.add("Access-Control-Allow-Origin", "*")
  response.headers.add("Access-Control-Allow-Headers", "*")
  response.headers.add("Access-Control-Allow-Methods", "*")
  return response

@app.route("/products/<user>", methods=['GET'])
def get_products(user):
  return response_wrapper(lambda : product_router.list(user))
  
@app.route("/products/<user>", methods=['POST'])
def post_products(user):
  return response_wrapper(lambda : product_router.add(user, request.json['products']))

@app.route("/products/<user>", methods=['DELETE'])
def delete_products(user):
  return response_wrapper(lambda : product_router.remove(user, request.json['products']))

@app.route("/recipe/<user>", methods=['GET'])
def recipe(user):
  return response_wrapper(lambda : product_router.search(user))


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return response_wrapper(lambda : {}, 404)

if __name__ == "__main__":
    app.run(debug=True)