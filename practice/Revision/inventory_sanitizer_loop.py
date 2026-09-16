server_inventory = ['srv-101', '  srv-102', 'srv-103  ', 'SRV-104', 'srv-105']
clean_inventory = []
for server in server_inventory:
    clean_server = server.strip()
    print(clean_server)
    lower_server = clean_server.lower()
    print(lower_server)
    clean_inventory.append(lower_server)
print(clean_inventory)