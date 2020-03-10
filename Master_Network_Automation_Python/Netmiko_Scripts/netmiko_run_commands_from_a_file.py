from netmiko import ConnectHandler
cisco_device = {
        'device_type': 'cisco_ios',
        'ip': '10.1.1.1',
        'username': 'u1',
        'password': 'cisco',
        'port': 22,
        'secret': 'cisco',
        'verbose':True
        }
connection = ConnectHandler(**cisco_device)

print('Entering enable mode ...')
connection.enable()

print('Running commands from file...')
output = connection.send_config_from_file('ospf.txt')
print(output)


connection.disconnect()