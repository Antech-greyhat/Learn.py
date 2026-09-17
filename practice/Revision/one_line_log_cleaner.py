
raw_ips = ['  192.168.1.100\n', '10.0.0.5  ', '  172.16.0.50\n']
#print(raw_ips)
clean_ips = [ip.strip() for ip in raw_ips]
print(clean_ips)