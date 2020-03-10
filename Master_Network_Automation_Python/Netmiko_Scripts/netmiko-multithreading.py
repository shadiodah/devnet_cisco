import threading
from netmiko import ConnectHandler

# Define username and password to login to all routers with
USER = 'u1'
PASSWORD = 'cisco'

routers = ['192.168.122.10', '192.168.122.11', '192.168.122.12', '192.168.122.13', '192.168.122.14']


def ssh_session(ip):
    router = {'device_type': 'cisco_ios', 'ip': ip, 'username': USER, 'password': PASSWORD, 'verbose': False }
    ssh_session = ConnectHandler(**router)
    output = ssh_session.send_command("show version")

    print(output)
    print('#' * 50)
    ssh_session.disconnect()


if __name__ == "__main__":
    import time
    start = time.perf_counter()

    # Create a thread for each device and add it to the list of threads
    threads = list()
    for ip in routers:
        my_thread = threading.Thread(target=ssh_session, args=(ip,))
        threads.append(my_thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    end = time.perf_counter()
    print(end-start)