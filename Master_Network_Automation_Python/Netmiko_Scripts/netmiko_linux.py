from netmiko import ConnectHandler
import logging


logging.basicConfig(filename='netmiko.log', level=logging.DEBUG)
logger = logging.getLogger('netmiko')


linux = {
        'device_type': 'linux',
        'ip': '192.168.0.16',
        'username': 'u2',
        'password': '1234',
        'port': 2299,
        'secret': '1234',         # Add the sudo password
        'verbose':True
        }

connection = ConnectHandler(**linux)

# Will execute 'sudo su' (will pass the secret as the password for the sudo)
connection.enable()
output = connection.send_command('ls -l /etc/ > /root/a.txt')
print(output)

connection.disconnect()