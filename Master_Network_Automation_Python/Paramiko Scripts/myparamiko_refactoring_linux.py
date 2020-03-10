import myparamiko
import getpass

password = getpass.getpass()

ssh_client = myparamiko.connect('192.168.0.133', 2299, 'andrei', password)
remote_connection = myparamiko.get_shell(ssh_client)
myparamiko.send_command(remote_connection,'sudo useradd -m -d /home/user2 -s /bin/bash user2')
myparamiko.send_command(remote_connection, password)
users = myparamiko.send_command(remote_connection,'cat /etc/passwd')

print(users.decode())
myparamiko.close(ssh_client)