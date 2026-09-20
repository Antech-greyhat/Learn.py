
import random
server_status = {
    'hostname': 'antech-master',
    'firewall': 'enabled'
}
active_ports = set()
for i in range(5):
    random_number = random.randint(8000,8005)
    active_ports.add(random_number)

server_status.update({'open_ports': active_ports})
print(server_status)
print(random_number)