from math import radians,sin,cos
import datetime
angle_degrees = 40
angle_radians = radians(angle_degrees)

sine_value = sin(angle_radians)
cos_value = cos(angle_radians)

print(sine_value) # 0.6427876096865393
print(cos_value) # 0.766044443118978

birthday = datetime.date(2007,12,7)
print(birthday.day) # 7
print(birthday.month) # 12
print(birthday.year) # 2007