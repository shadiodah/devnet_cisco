f = open('router.txt') #open file in read-only mode

#looping throuth the file and printing the file line by line
for line in f:
    print(line, end='') #by default print uses \n at the end of the printed line

#file must be closed
f.close()