
while True:
    command: str = input('Antech-shell>:')
    clean_command = command.strip().lower()
    if clean_command == "":
        print('Command cannot be blank')
        continue
    if clean_command == 'help':
        print('Available commands: scan, help, exit')
        continue
    elif clean_command == "scan":
        print('Initiating network scan...')
    elif clean_command == 'exit':
        print('Terminating session...')
        break
    else:
        print('Error: Unknown command')