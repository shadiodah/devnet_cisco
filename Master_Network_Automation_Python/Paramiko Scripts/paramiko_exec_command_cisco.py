import paramiko

ssh_client = paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect('10.1.1.1', port=22, username='andrei', password='cisco', look_for_keys=False, allow_agent=False)

stdin, stdout, stderr = ssh_client.exec_command('sh version')


output = stdout.read().decode()
print(output)

ssh_client.close()

with open('R1_show_version.txt', 'w') as f:
    f.write(output)