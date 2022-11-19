start_products = ['tomato', 'cheese', 'pasta']
# import json
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
    if ref.get() is None:
      ref.set(start_products)
    return ref

  def list(self, user):
    ref = self.get_user(user)
    return self.get_ref_for(user).get()

  def add(self, user, new_products):
    ref = self.get_user(user)
    products = list(set(ref.get()) | set(new_products))
    ref.set(products)
    

  def remove(self, user, removed_products):
    ref = self.get_user(user)
    products = list(set(ref.get()) - set(removed_products))
    ref.set(products)



# cred_obj = fa.credentials.Certificate('./credentials/fridgefront-a501e-firebase-adminsdk-xvue4-b225b21e7b.json')
# fa.initialize_app(cred_obj, {'databaseURL': "https://fridgefront-a501e-default-rtdb.firebaseio.com"})


# ref = db.reference("/")
# ref.set({
# 	"Users":
# 	{
# 		"hifhiu3h8-34n3ihb-di3hd": [
#       'tomato',
#       'cheese'
#     ]
# 	}
# })

# ref = db.reference("/Users/hifhiu3h8-34n3ihb-di3hd")
# ref.set(['tomato'])