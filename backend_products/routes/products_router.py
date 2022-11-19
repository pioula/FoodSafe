start_products = ['tomato', 'cheese', 'pasta']
import json
import firebase_admin as fa
from firebase_admin import db


class ProductRouter():
  def __init__(self):
    self.products = dict()
    cred_obj = fa.credentials.Certificate('./credentials/fridgefront-a501e-firebase-adminsdk-xvue4-b225b21e7b.json')
    fa.initialize_app(cred_obj, {'databaseURL': "https://fridgefront-a501e-default-rtdb.firebaseio.com"})
    self.db = db.reference('/')

  def ensure_user_exists(self, user):
    if self.products.get(user) is None:
      self.db.set(json.dumps(dict({user: start_products})))
      self.products[user] = start_products

  def list(self, user):
    self.ensure_user_exists(user)
    # return self.products[user]
    return self.db.get(user)

  def add(self, user, new_products):
    self.ensure_user_exists(user)
    self.products[user] = self.products[user] | set(new_products)

  def remove(self, user, removed_products):
    self.ensure_user_exists(user)
    self.products[user] = self.products[user] - set(removed_products)


