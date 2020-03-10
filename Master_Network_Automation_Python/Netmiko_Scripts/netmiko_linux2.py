from netmiko import ConnectHandler

linux = {
        'device_type': 'linux',
        'ip': '192.168.0.134',
        'username': 'andrei',
        'password': 'test1234',
        'port': 2299,
        'secret': 'test1234', #sudo password
        'verbose':True
        }
connection = ConnectHandler(**linux)

connection.enable()
output = connection.send_command('apt-get update && apt-get -y install apache2')
print(output)


connection.disconnect()