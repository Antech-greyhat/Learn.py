# practising enumerate().

target_queue = ['192.168.1.10', '10.0.0.5', '172.16.0.2']
for index,target in enumerate(target_queue):
    print(f'scanning target at index {index}: {target}')

cars_priority = ['mazda', 'audi', 'wish', 'mercedes', 'toyota', 'isuzu']
for index,car in enumerate(cars_priority):
    print(f'Car at index: {index} is {car}')