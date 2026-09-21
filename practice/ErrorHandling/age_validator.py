
def check_age(age):
    if age < 0 or age > 120:
        raise ValueError(f"Invalid Age: {age}")
    return age
print("--- Running Test 1. (Bad Value)---")
try:
    bad_age = check_age(-5)
    print(f"Success! Age is Verified as: {bad_age}")
except ValueError as e:
    print(f'Age check failed: {e}')

print('---running Test 2 ----')

try:
    good_age = check_age(30)
    print(f'Success Age verified as: {good_age}')
except ValueError as e:
    print(f'Age check failed! Error: {e}')