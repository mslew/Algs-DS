#Author: Max Lewis
#This program will modify the experiment from Code Fragment 5.1 in order to demonstrate the Python's list class occasionally shrinks the size of its underlying array
#when elements are popped from a list. 

import sys

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20]
n = 10
for k in range(n):
    data = data[:len(data)]
    data.pop()
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Size in Bytes: {1:4d}'.format(a, b))
