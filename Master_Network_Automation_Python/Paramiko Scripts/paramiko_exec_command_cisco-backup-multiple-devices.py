import myparamiko

devices = ['10.1.1.10', '10.1.1.20', '10.1.1.30']
for device in devices:
    ssh_client = myparamiko.connect(device, 22, 'andrei', 'cisco')
    remote_connection = myparamiko.get_shell(ssh_client)
    myparamiko.send_command(remote_connection, 'enable')
    myparamiko.send_command(remote_connection, 'cisco')
    myparamiko.send_command(remote_connection, 'terminal length 0')
    output = myparamiko.send_command(remote_connection,'show run')

    output_str = output.decode()
    #print(output_str)

    list = output_str.split('\n')
    list = list[4:-1]
    config = '\n'.join(list)
    #print(config)

    #10.1.1.10-2018-09-24.txt
    import datetime
    now = datetime.datetime.now()
    today = str(now.year) + '-' + str(now.month) + '-' + str(now.day)
    file = device + '-' + today + '.txt'
    with open(file, 'w') as f:
        print('Saving configuration of ' + device)
        f.write(config)
        print('Ok')
    myparamiko.close(ssh_client)

