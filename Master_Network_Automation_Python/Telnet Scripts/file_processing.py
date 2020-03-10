with open('devices.txt', 'r') as f:
    d = f.read().splitlines()
    print(d)

ip = list()
for item in d:
    x = item.split(':')
    print(f'x= {x}')
    ip.append(tuple(x))
    print(ip)

print(ip)