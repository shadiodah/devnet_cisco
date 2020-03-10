import myparamiko


ssh_client = myparamiko.connect('10.1.1.10', 22, 'andrei', 'cisco')
remote_connection = myparamiko.get_shell(ssh_client)
myparamiko.send_command(remote_connection, 'enable')
myparamiko.send_command(remote_connection, 'cisco')
myparamiko.send_command(remote_connection, 'terminal length 0')
output = myparamiko.send_command(remote_connection,'show run')

output_str = output.decode()
print(output_str)

list = output_str.split('\n')
list = list[4:-1]
config = '\n'.join(list)
#print(config)

with open('Router1-running-config.txt', 'w') as f:
    f.write(config)

myparamiko.close(ssh_client)

