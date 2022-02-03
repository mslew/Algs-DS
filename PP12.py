#Author: Max Lewis
#Determine the amount of inversions in a list.

def inversions(l):
    p1 = 0
    p2 = len(l) - 1
    inversions = 0
    while p1 != p2:
        if l[p1] > l[p2]:
            inversions += 1
        if p1 + 1 == p2:
            p1 += 1
            p2 = len(l) - 1
        else:
            p2 -= 1          
    return inversions

if __name__ == '__main__':
    l = [1,2,4,5,3]
    print(inversions(l))
