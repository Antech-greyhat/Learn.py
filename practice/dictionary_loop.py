# They are helpful for updating their values or applying some logic to them

products ={
    'laptop': 1000,
    'smartphone': 600,
    'tablet': 300,
    'headphones': 100
}
# printing the values using for loop.
for price in products.values():
    print(price)

#printing the keys and corresponding values.
for price in products.keys():
    print(price)

# storing key and value in separate loop variables.
for product,price in products.items():
    print(product,price)

# assigning 20 %  to discount to our items were we will multiply by 0.8
for product,price in products.items():
    products[product] = round(price * 0.8)
print(products)

# we can use enumerate() to iterate over the key-value pairs.
for product in enumerate(products):
    print(product)