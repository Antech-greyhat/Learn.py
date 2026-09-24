# Review on Error Handling
prices = ['12.50','8.99','abc','5.00']
converted_values = []
for item in prices:
    try:
        values = float(item)
        converted_values.append(values)
    except ValueError as e:
        print(f"{e} Skipping....")
print(f"Final List: {converted_values}")