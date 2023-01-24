from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import redis
import pickle

r = redis.Redis(
  host="redis.fridge.svc.cluster.local",
  port=6379,
  db=0, password=None
)

expiry_time = 30

# Przyjmuje listę produktów np. ["tomato", "apple"]
def get_recipes_by_products(products):
  results = requests.get(
    'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients',
    {
      'ingredients': ','.join(products),
      'ranking': '1',
      'ignorePantry': 'true',
      'number': '1'
    },
    headers={
      'X-RapidAPI-Key': 'e5fca8677fmsh3fb1abe4853bc35p190616jsna17f05ce9330', # Zmienić api key
      'X-RapidAPI-Host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com'
    }
  )
  return results.json()

def get_data_from_recipe(id):
  result = requests.get(
    'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{}/information'.format(id),
    headers={
      'X-RapidAPI-Key': 'e5fca8677fmsh3fb1abe4853bc35p190616jsna17f05ce9330',
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

def search(products):
  if len(products) == 0:
    products = ['tomato', 'pasta']
  products.sort()

  recipe_counter = dict()
  for product in products:
    id = r.get(product)
    if id != None:
      recipe_counter[id] = recipe_counter.get(id, 0) + 1

  recipe_counter = recipe_counter.items()
  if len(recipe_counter) > 0:
    best_match = (None, 0)
    for id, count in recipe_counter:
      if count > best_match[1]:
        best_match = (id, count)
    recipe = r.get(best_match[0])
    print('cached:', best_match)
    return dict(enumerate([pickle.loads(recipe)]))

  recipes = get_recipes_by_products(products)
  results = []
  for meal in recipes:
    id = meal['id']
    result = get_data_from_recipe(id)
    result['missed_ingredients'] = [ing['name'] for ing in meal['missedIngredients']]
    results.append((id, result))

  id, result = results[0]
  r.set(name=id, value=pickle.dumps(result), ex=expiry_time+5)
  print('set id:', id)

  for product in products:
    r.set(name=product, value=id, ex=expiry_time)
    print('set prod:', product)

  print(dict(enumerate(results)))
  return dict(enumerate(results))

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
  
@app.post("/recipe")
def get_recipe(body: Products):
  return search(body.products)

