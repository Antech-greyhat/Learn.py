# Scope determines where you can use your variable in your code.
# 1. Global Scope - a variable created outside a function. you can use it both inside and outside a function.
# example:

tax_rate = 0.01

def calculate_tax(price):
    tax = price * tax_rate
    return tax
print(tax_rate) # output: 0.01

# 2. Local Scope - a variable created inside a function. you can only use it inside that function.
# function parameters are local variables too.

rate_tax = 0.02
def calculated_tax(prices):
    taxed = prices * rate_tax
    return taxed
print(tax_rate) #0.01
print(taxed) #output: NameError: name 'taxed' is not defined