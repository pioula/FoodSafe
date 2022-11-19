start_products = set(['tomato', 'cheese', 'pasta'])

class ProductRouter():
  def __init__(self):
    self.products = dict()

  def ensure_user_exists(self, user):
    if self.products.get(user) is None:
      self.products[user] = start_products

  def list(self, user):
    self.ensure_user_exists(user)
    return self.products[user]

  def add(self, user, new_products):
    self.ensure_user_exists(user)
    self.products[user] = self.products[user] | set(new_products)

  def remove(self, user, removed_products):
    self.ensure_user_exists(user)
    self.products[user] = self.products[user] - set(removed_products)



