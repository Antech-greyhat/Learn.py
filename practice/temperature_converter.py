
temperature = input('Enter your temperature range from 0 - 100:')
unit = input('Enter temperature units C or F:')
temperature = float(temperature)
print(temperature)
print(type(temperature))
final_unit = unit.lower()

if final_unit == 'c':
    converted = 9/5 + 32
    print(f'{temperature} C is {converted} F')
else:
    converted = (temperature - 32) * 5/9
    print(f'{temperature} F is {converted} C')

if not isinstance(temperature,int):
    print('Temperature should be integer ranges from 0 - 100')
else:
    print('Temperature recorded')

if not isinstance(final_unit,str):
    print('Units must be string C or F')
else:
    print('Units recorded')
if final_unit != 'c' and unit != 'f':
    print('Units should be C or F')
if final_unit == 'c':
    celsius_value = temperature
else:
    celsius_value = converted

if celsius_value < 0:
    print("That's freezing!")
elif celsius_value < 20:
    print("Nice and cool")
elif celsius_value < 30:
    print("Nice and warm")
else:
    print("Scorching!")

#print(temperature)
#print(unit)