from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pymongo import MongoClient

def get_database(uid):
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   
   CONNECTION_STRING = "mongodb://mongo:pass@mongo-0.mongo-svc:27017"
   a = uid[0]
   if a.islower() or (a.isnumeric() and a <= '4'):
    CONNECTION_STRING = "mongodb://mongo:pass@mongo-1.mongo-svc:27017"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['food_safe']

def get_user_table(uid):
   db = get_database(uid)
   return db["user_items"]

def get_user_products(uid):
  col = get_user_table(uid)
  user_info = col.find({"uid": uid})
  user_info_list = list(user_info)
  if len(user_info_list) == 0:
    return []
  else:
    return user_info_list[0]["products"]

def set_user_products(uid, products):
  col = get_user_table(uid)
  if len(list(col.find({"uid": uid}))) == 0:
    return col.insert_one({"uid": uid, "products": products})
  else:
    return col.update_one({"uid": uid}, {"$set": {"products": products}})

def list_to_lower(list):
  return [e.lower() for e in list]

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Products(BaseModel):
  products: list

def set_products(user, products):
  set_user_products(user, products)
  return {}

@app.get("/products/{uid}")
def get_products_query(uid):
  return {'products': get_user_products(uid)}

@app.post("/products/{uid}")
def add_products_query(uid, body: Products):
  return set_products(uid, list(set(get_user_products(uid)) | set(list_to_lower(body.products))))

@app.delete("/products/{uid}")
def delete_products_query(uid, body: Products):
  return set_products(uid, list(set(get_user_products(uid)) - set(list_to_lower(body.products))))