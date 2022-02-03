#Author: Max Lewis
#This program will take two sorted lists and merge them into one list, sorted, in one pass.

def merge(l1, l2):
    l = [] 
    i = 0
    k = 0
    while i < len(l1) and k < len(l2): #stops when the shortest list is done iterating
        if l1[i] < l2[k]: #compare elements 
            l.append(l1[i]) #add smallest element
            i += 1
        else:
            l.append(l2[k]) #add smallest element
            k += 1
    l = l + l1[i:] + l2[k:] #add the rest of both lists 
    return l



if __name__  == '__main__':
    l1 = [1, 2, 66, 4, 2, 34, 5, 5, 2, 2, 5, 67, 46, 5, 2, 2, 5, 6, 3, 2, 5]
    l2 = [6, 35, 354, 536, 352, 24, 25, 6, 5, 65, 34, 234, 45, 64, 234]
    l1.sort()
    l2.sort()
    print(merge(l1, l2))