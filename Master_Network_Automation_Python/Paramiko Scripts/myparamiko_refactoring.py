import myparamiko

ssh_client = myparamiko.connect('10.1.1.1', 22, 'andrei', 'cisco')
remote_connection = myparamiko.get_shell(ssh_client)
myparamiko.send_command(remote_connection, 'enable')
myparamiko.send_command(remote_connection,'cisco')
myparamiko.send_command(remote_connection,'terminal length 0')
output = myparamiko.send_command(remote_connection,'show run')
print(output.decode())
myparamiko.close(ssh_client)