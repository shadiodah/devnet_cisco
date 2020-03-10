# f = open('router.txt', 'rt', encoding='utf-8')
#
# content = f.read()
# print(content)
#
# print(f.closed)
# f.close()

# with open('router.txt') as f:
#     content = f.read()
#     print(content)
#
# print('File is closed: ', f.closed)

with open('router.txt') as f:
    #list1 = list(f)
    #list1 = f.readlines()
    # for line in f:
    #     print(line, end='')

    list1 = f.read().splitlines()
    #print(list1)
    for item in list1:
        print(item)


#print(list1)


