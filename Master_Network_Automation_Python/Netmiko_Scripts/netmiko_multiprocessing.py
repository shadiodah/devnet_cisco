from netmiko import ConnectHandler
import multiprocessing as mp
import time


def connect_and_run(device, cmd='show run'):
    print('Connecting to device: ', device['ip'])
    connection = ConnectHandler(**device)

    print('Entering enable mode ...')
    connection.enable()

    print('Executing command: ', cmd)
    output = connection.send_command(cmd)
    print(output)
    print('#' * 40)


if __name__ == '__main__':
    with open('devices.txt') as f:
        devices = f.read().splitlines()

    device_list = list()

    for ip in devices:
        cisco_device = {
            'device_type': 'cisco_ios',
            'ip': ip,
            'username': 'andrei',
            'password': 'cisco',
            'port': 22,
            'secret': 'cisco', #this is the enable password
            'verbose': True
        }
        device_list.append(cisco_device)

    #print(device_list)

    #script starting time
    start = time.time()

    processes = list()
    for device in device_list:
        processes.append(mp.Process(target=connect_and_run, args=(device, 'sh run')))


    for p in processes:
        p.start()


    for p in processes:
        p.join()

    #script ending time
    end = time.time()

    print('Script execution time:', end - start)