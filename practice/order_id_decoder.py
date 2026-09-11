
home_state = "NY"

def check_shipping_zone(tracking_id):
    if not tracking_id:
        return 'Invalid code'
    state_code = tracking_id[10:12]

    if state_code == home_state:
        return 'This is local delivery'
    else:
        return 'this is out of state'

print(check_shipping_zone("SHIP-6789-NY-PRIORITY"))
print(check_shipping_zone("SHIP-6666-CA-PRIORITY"))
print(check_shipping_zone(""))