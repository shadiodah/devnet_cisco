with open('devices.txt','r') as f:      #when opening a file using with keyword it doesn't have to manually close it
    #device is list, each element is a line from the file
    device = f.read().splitlines()
#print(device)

ip = list()
#iterate through the devices list and split each element using the : as a separator
for item in device:
    tmp = item.split(':')
    ip.append(tuple(tmp))


print(ip)