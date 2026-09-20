# practice on sets
raw_logs_ips = ['192.168.1.1', '10.0.0.1', '192.168.1.1', '172.16.0.5', '10.0.0.1', '192.168.1.1']

unique_ips = set(raw_logs_ips)
print(unique_ips)

unique_ips.add('192.168.1.50')
print(unique_ips)

# python will silently ignore this duplicate and will not throw an error:
unique_ips.add('10.0.0.1')
print(unique_ips)

print(f'The unique Ips assigned are: {unique_ips}')
print(f'the length of the unique Ips is: {len(unique_ips)}')