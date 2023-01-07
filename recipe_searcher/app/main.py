from fastapi import FastAPI
from pydantic import BaseModel
import requests
import redis
import pickle

r = redis.Redis(
  host="redis",
  port=6379,
  db=0, password=None
)

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
  recipe = r.get(products[0])
  if recipe != None:
    return dict(enumerate([pickle.loads(recipe)]))
  recipes = get_recipes_by_products(products)

  results = []
  for meal in recipes:
    id = meal['id']
    result = get_data_from_recipe(id)
    result['missed_ingredients'] = [ing['name'] for ing in meal['missedIngredients']]
    results.append(result)
  r.set(name=products[0], value=pickle.dumps(results[0]), ex=15)
  return dict(enumerate(results))

app = FastAPI()

class Products(BaseModel):
  products: list
  
@app.post("/recipe")
def get_recipe(body: Products):
  return search(body.products)

