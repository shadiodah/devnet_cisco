from netmiko import ConnectHandler

cisco_device = {
        'device_type': 'cisco_ios',
        'ip': '10.1.1.10',
        'username': 'u1',
        'password': 'cisco',
        'port': 22,
        'secret': 'cisco',
        'verbose':True
        }

connection = ConnectHandler(**cisco_device)

connection.enable()

commands = ['int loopback 1', 'ip address 7.7.7.7 255.255.255.255', 'exit', 'username user4 secret cisco']
output = connection.send_config_set(commands)
print(output)


output = connection.send_command_expect('write memory')
print(output)

connection.disconnect()