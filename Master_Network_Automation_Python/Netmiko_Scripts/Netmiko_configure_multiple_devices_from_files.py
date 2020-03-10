from netmiko import ConnectHandler
import time

with open('devices1.txt') as f:
    devices = f.read().splitlines()

device_list = list()
for ip in devices:
    cisco_device = {
            'device_type': 'cisco_ios',
            'ip': ip,
            'username': 'cisco',
            'password': 'cisco',
            'port': 22,
            'secret': 'cisco', #this is the enable password
            'verbose': True
            }
    device_list.append(cisco_device)

#print(device_list)
for device in device_list:
    print('Connecting to ' + device['ip'])
    connection = ConnectHandler(**device)
    time.sleep(3)
    print('Entering enable mode ...')
    connection.enable()
    time.sleep(3)

    file = input('Enter configuration file (use a valid path) for ' + device['ip'] +':')

    print('Running commands from file:', file, 'to device:', device['ip'])
    output = connection.send_config_from_file(file)
    time.sleep(3)
    print(output)

    connection.disconnect()