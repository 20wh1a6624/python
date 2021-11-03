def linear_search(list,ele):
    for i in range(len(list)):
        if list[i] == ele:
            return i
    return -1

list = list(map(int(input('enter')))).split()
ele = int(input('enter element that need to be found'))

pos = linear_search(list,ele)
if pos == -1:
    print( 'element not found')
else:
    print ('element foud  at position',pos)


