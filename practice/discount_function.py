def apply_discount(price,discount):
    if not isinstance(price, (int,float)):
        return 'The price should be a number'
    if not isinstance(discount, (int,float)):
        return 'The discount should be a number'
    if price < 0:
        return 'Price should be greater than 0'
    if discount < 0 or discount > 100:
        return 'Discount should be between 0 and 100'
    return price * (1 - discount /100)
result = apply_discount(100,50)
print(result)