
while True:
    port_input = input("Enter Target Port Number (1-65535): ")
    try:
        target_port = int(port_input)
        if 1 <= target_port <= 65535:
            print(f"Configuration saved: {target_port} is targeted")
            break
        else:
            print('Port must be between (1 and 65535)')
    except ValueError:
        print('Invalid Input! Please Enter Number Only')