from netmiko import ConnectHandler
import time
from termcolor import cprint
import multiprocessing as mp


def connect_and_run(device, cmd):
    cprint('Connecting to ' + device['ip'], 'red')
    connection = ConnectHandler(**device)

    print('Entering enable mode ...')
    connection.enable()
    time.sleep(3)
    print('Logged in to Router ' + device['ip'])

    output = connection.send_command(cmd)
    # print(output)

    prompt = connection.find_prompt()
    # print(prompt)
    hostname = prompt[:-1]
    # print(hostname)

    list = output.split('\n')
    list = list[3:]
    # print(list)
    config = '\n'.join(list)
    # print(config)

    import datetime
    now = datetime.datetime.now()
    today = str(now.year) + '-' + str(now.month) + '-' + str(now.day)
    file = today + '-' + hostname + '.txt'

    with open(file + '.txt', 'w') as backup:
        backup.write(config)
        cprint('Backup of ' + hostname + ' completed successfully', attrs=['bold'])
        cprint('#' * 30, attrs=['bold'])

    connection.disconnect()


if __name__ == '__main__':
    with open('devices_backup.txt') as f:
        file_content = f.read().splitlines()    # file_content is a list
    #print(file_content)

    devices = list()
    for item in file_content:
        tmp = item.split(':')  # tmp is a list
        devices.append(tmp)
    #print(devices)

    device_list = list()
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
        device_list.append(net_device)
    #print(device_list)

    processes = list()
    for device in device_list:
        processes.append(mp.Process(target=connect_and_run, args=(device ,'sh run')))

    for p in processes:
        p.start()

    for p in processes:
        p.join()
