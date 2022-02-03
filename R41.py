def find_max(l):
    if len(l) == 1:
        return l[0]
    else:
        max = find_max(l[1:])
        return max if max > l[0] else l[0]

if __name__ == '__main__':
    l = [3,2,3,4,5,6,4,3,2,2,3,5,5]
    print(find_max(l))

#this program's run time and space complexity is O(n)