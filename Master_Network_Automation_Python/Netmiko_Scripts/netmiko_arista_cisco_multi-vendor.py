from netmiko import ConnectHandler

with open('devices.txt') as f:
    file_content = f.read().splitlines()


devices = list()
for item in file_content:
    tmp = item.split(':')  #tmp is a list
    devices.append(tmp)


for device in devices:
    net_device = {
        'device_type': device[0],
        'ip': device[1],
        'username': device[2],
        'password': device[3],
        'port': 22,
        'secret': device[3],  # this is the enable password
        'verbose': True
    }

    connection = ConnectHandler(** net_device)

    if not connection.check_enable_mode():
        connection.enable()


    #connection.config_mode()
    config_file = input('Enter configuration file for device type ' + device[0] + ' with ip ' + device[1])
    print('Sending commnands to device ...')
    with open(config_file) as config:
        commands = config.read().splitlines()
    # print(commands)

    output = connection.send_config_set(commands)
    print(output)
    print('Disconecting ....')
    print('#' * 40)


    connection.disconnect()