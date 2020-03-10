import paramiko
from scp import SCPClient

ssh_client = paramiko.SSHClient()
ssh_client.load_system_host_keys()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='192.168.0.133', port=2299, username='andrei', password='mypass123', allow_agent=False, look_for_keys=False)


scp = SCPClient(ssh_client.get_transport())

#copy a single file
#scp.put('devices.txt', 'aa.txt')

#copy a directory
#scp.put('directory1', recursive=True, remote_path='/tmp')

scp.get('/etc/passwd','C:\\Users\\ad\\passwd-from-linux.txt')
scp.close()