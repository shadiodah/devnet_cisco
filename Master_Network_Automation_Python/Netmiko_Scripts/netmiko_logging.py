from netmiko import ConnectHandler
import logging


#startind logging (in test.log in the current working dir)
logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")


cisco_device = {
        'device_type': 'cisco_ios',
        'ip': '10.1.1.1',
        'username': 'andrei',
        'password': 'cisco',
        'port': 22,
        'secret': 'cisco',
        'verbose':True
        }

connection = ConnectHandler(**cisco_device)

output = connection.send_command('show version')
print(output)

connection.disconnect()