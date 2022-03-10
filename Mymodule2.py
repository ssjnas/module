class Cart:
   flat_discount = 0
   min_bill = 100
   def __init__(self):
       self.items = {}
   def add_item(self, item_name,quantity):
       self.items[item_name] = quantity
   def display_items(self):
       return (self.items)
   @classmethod
   def update_flat_discount(cls, 
                          new_flat_discount):
       cls.flat_discount = new_flat_discount
   @staticmethod
   def greet():
       print("Have a Great Shopping")
a = Cart()
a.add_item("book", 3)
a.display_items()
Cart.update_flat_discount(25)
Cart.greet()
