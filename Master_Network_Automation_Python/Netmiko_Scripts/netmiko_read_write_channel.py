from netmiko import ConnectHandler
import time

device = {
        'device_type': 'cisco_ios',
        'ip': '10.1.1.1',
        'username': 'andrei',
        'password': 'cisco',
        'port': 22,
        'secret': 'cisco',
        'verbose':True
        }

connection = ConnectHandler(**device)
connection.enable()

connection.write_channel('show run\n')
time.sleep(3)

output = connection.read_channel()
print(output)

connection.disconnect()