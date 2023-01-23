connString = 'mongodb://mongo:pass@localhost:27017'

from pymongo import MongoClient
def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = connString
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['fridgeSafe']
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
  # Get the database
  dbname = get_database()
  print(dbname)
  collection_name = dbname["user_items"]
  print(collection_name)
  collection_name.insert_one({"products": ["tomato", "penne"]})
  
  item_details = collection_name.find()
  print(item_details)
  for item in item_details:
    # This does not give a very readable output
    print(item)