from netmiko import Netmiko
from netmiko import ConnectHandler

#connection = Netmiko(host='10.1.1.1', username='u1', password='cisco', device_type='cisco_ios')

cisco_device = {
        'device_type': 'cisco_ios',
        'ip': '10.1.1.10',
        'username': 'andrei',
        'password': 'cisco',
        'port': 22,
        'secret': 'cisco',
        'verbose':True
        }

connection = ConnectHandler(**cisco_device)

prompt = connection.find_prompt()
print(prompt)
if '>' in prompt:
    connection.enable()

prompt = connection.find_prompt()
print(prompt)

output = connection.send_command('sh run')
print(output)


mode = connection.check_config_mode()
if not mode:
    connection.config_mode()

mode =  connection.check_config_mode()
print(mode)

#output = connection.send_command('username user2 secret cisco')

connection.disconnect()