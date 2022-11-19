start_products = ['tomato', 'cheese', 'pasta']
import requests
import json
import firebase_admin as fa
from firebase_admin import db


class ProductRouter():
  def __init__(self):
    self.products = dict()
    cred_obj = fa.credentials.Certificate('./credentials/fridgefront-a501e-firebase-adminsdk-xvue4-b225b21e7b.json')
    fa.initialize_app(cred_obj, {'databaseURL': "https://fridgefront-a501e-default-rtdb.firebaseio.com"})

  # returns any reference for user
  def get_ref_for(self, user):
    return db.reference('/Users/{}'.format(user))

  # returns validated reference for user
  def get_user(self, user):
    ref = self.get_ref_for(user)
    products = ref.get()
    if products is None:
      products = []
    return ref, products

  def list(self, user):
    _, products = self.get_user(user)
    return products

  def add(self, user, new_products):
    ref, products = self.get_user(user)
    products = list(set(products) | set(new_products))
    ref.set(products)

  def remove(self, user, removed_products):
    ref, products = self.get_user(user)
    products = list(set(products) - set(removed_products))
    ref.set(products)

  def search(self, user):
    ref, products = self.get_user(user)
    xd = requests.get(
      'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients',
      {
        'ingredients': ','.join(products),
        'ranking': '1',
        'ignorePantry': 'true',
        'number': '5'
      },
      headers={
        'X-RapidAPI-Key': '5c1cef73cfmsh554db8e0a00da8fp1f020ajsn5700fe68f2bc',
        'X-RapidAPI-Host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com'
      }
    )
    xd = dict(enumerate(xd.json()))
    # print(xd)
    # print(','.join(products))
    return xd

# results -> 0 -> analyzedInstructions -> 0 -> steps -> 0..n -> step NIE
# results -> 0 -> creditsText TAK
# results -> 0 -> extendedIngredients -> 0..n -> original (to jest nazwa oraz ilość) TAK
# results -> 0 -> missedIngredients -> 0..n -> name (to jest krótka nazwa) TAK
# results -> 0 -> image TAK
# results -> 0 -> sourceUrl TAK
# results -> 0 -> summary TAK
# 
