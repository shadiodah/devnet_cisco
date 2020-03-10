import myparamiko
import getpass

username = input('Username:')
password = getpass.getpass()

ssh_client = myparamiko.connect('192.168.0.133', 2299, username, password)
remote_connection = myparamiko.get_shell(ssh_client)

new_user = input('Enter the user you want to create:')
command = 'sudo useradd -m -d /home/' + new_user + ' -s /bin/bash ' + new_user
myparamiko.send_command(remote_connection, command)
myparamiko.send_command(remote_connection, password)
print('A new user has been created.')

answer = input('Display the users ? <y|n>')
if answer == 'y':
    users = myparamiko.send_command(remote_connection,'cat /etc/passwd')
    print(users.decode())


myparamiko.close(ssh_client)