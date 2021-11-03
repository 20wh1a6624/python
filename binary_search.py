def binary_search(lst,element,high,low):
    while(low <= high):
        mid = (low + high) // 2
        if lst[mid] < element:
            low = mid + 1
        if lst[mid] > element:
            high = mid - 1
        if lst[mid] == element:
            return mid
    return -1
n = int(input('enter no of ele')
lst = list(map(int, input('enter ele').split()))))
element = int(input('enter ele'))

l = 0
h = n - 1
pos = binary_search(a,l,h,key)
if pos == -1:
    print('ele not found')
else:
    print('ele found at 'pos + 1)

