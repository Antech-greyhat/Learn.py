
distance_mi = 9
is_raining = False
has_bike = True
has_car = False
has_ride_share_app = True

# 2. Evaluate categories in ascending order
if not distance_mi:
    # If distance_mi is a falsy value (0, None, empty)
    print(False)

elif distance_mi <= 1:
    # If distance is <= 1 mile
    if not is_raining:
        print(True)
    else:
        print(False)

elif distance_mi <= 6:
    # If distance is > 1 and <= 6 miles
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)

else:
    # If the distance is > 6 miles
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)