class Shopping:
    def __init__(self,item,price):
        self.item = item
        self.price = price
        self.time_cooked = 0

    def buying(self):
        return f'{self.item} and {self.price} are important'

    def cooked(self):
        self.time_cooked += 1
        return f"{self.item} has been Cooked {self.time_cooked}"
shopping_obj = Shopping('Rice',150)
shopping_obj1 = Shopping('Flour',200)

print(f"Am going to buy {shopping_obj.item} at Ksh: {shopping_obj.price}")
print(f"\nI will cook {shopping_obj1.item} it cost Ksh: {shopping_obj1.price}")

print(shopping_obj.buying())
print(shopping_obj1.buying())

print(shopping_obj1.cooked())
print(shopping_obj1.cooked())
print(shopping_obj1.cooked())
print(shopping_obj.cooked())