antech_server = {
    'os': 'kali_linux',
    'ip_address': '192.168.1.50',
    'firewall': 'active'
}
print(antech_server)
antech_server.update({'ip_address': '10.0.0.99'})
print(antech_server)

for key,value in antech_server.items():
    print(f'system {key} is set to {value}\n')