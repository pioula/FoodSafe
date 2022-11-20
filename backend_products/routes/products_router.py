start_products = ['tomato', 'cheese', 'pasta']
import requests
import json
from datetime import date
import firebase_admin as fa
from firebase_admin import db

def get_recipes_by_products(products):
  results = requests.get(
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
  return results.json()

def get_data_from_recipe(id):
  result = requests.get(
    'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{}/information'.format(id),
    headers={
      'X-RapidAPI-Key': '5c1cef73cfmsh554db8e0a00da8fp1f020ajsn5700fe68f2bc',
      'X-RapidAPI-Host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com'
    }
  )
  result = result.json()
  return {
    'ingredients': [ing['original'] for ing in result['extendedIngredients']],
    'image': result['image'],
    'summary': result['summary'],
    'sourceUrl': result['sourceUrl'],
    'title': result['title'],
    'creditsText': result['creditsText']
  }

class ProductRouter():
  def __init__(self):
    self.products = dict()
    cred_obj = fa.credentials.Certificate('./credentials/fridgefront-a501e-firebase-adminsdk-xvue4-b225b21e7b.json')
    fa.initialize_app(cred_obj, {'databaseURL': "https://fridgefront-a501e-default-rtdb.firebaseio.com"})

  # returns any reference for user
  def get_ref_for(self, user):
    return db.reference('/Users/{}'.format(user))

  # returns validated reference for user with fridge contents
  def get_user(self, user):
    ref = self.get_ref_for(user)
    products = ref.get()
    if products is None:
      products = []
    return ref, products

  # products with expiry date form a list 
  def list(self, user):
    _, products = self.get_user(user)
    products = [(product[0], product[1]) for product in products]
    products.sort(key=lambda x: date.fromisoformat(x[1]))
    return dict({'products': products})

  def add(self, user, new_products):
    ref, products = self.get_user(user)
    # new_products = [(d[0], date.fromisoformat(d[1])) for d in new_products]
    products = [(e[0], e[1]) for e in products + new_products]
    products = list(set(products))
    ref.set(products)
    return {}

  def remove(self, user, removed_products):
    ref, products = self.get_user(user)
    products = [(e[0], e[1]) for e in products]
    removed_products = [(e[0], e[1]) for e in removed_products]
    products = list(set(products) - set(removed_products))
    ref.set(products)
    return {}

  def search(self, user):
    _, products = self.get_user(user)
    n = len(products)
    for i in range(1, 4):
      current_products = [e[0] for e in products[:i*n/4]]

    recipes = get_recipes_by_products(products)
    results = []
    for meal in recipes:
      id = meal['id']
      result = get_data_from_recipe(id)
      result['missed_ingredients'] = [ing['name'] for ing in meal['missedIngredients']]
      results.append(result)

    return dict(enumerate(results))

