# with open('devices.txt') as f:
#     devices = f.read().splitlines()
#     #print(devices)
#
# mylist = list()
# for item in devices:
#     tmp = item.split(':')
#     mylist.append(tmp)
#
# print(mylist)

import csv
#devices.txt must be in the same directory
with open('devices.txt') as f:
    #create a reader object using the : as a delimiter (by default it uses , )
    reader = csv.reader(f, delimiter=':')
    #create am empty list
    mylist = list()
    #iterate through the reader and apppend each row (which is another list) to mylist
    for row in reader:
       mylist.append(row)


    print(mylist)
