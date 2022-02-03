def find_max(l):
    if len(l) == 2:
        if l[0] > l[1]:
            return l[0]
        else:
            return l[1]
    rest = find_max(l[1:])
    if l[0] > rest:
        return l[0]
    else:
        return rest

def find_min(l):
    if len(l) == 2:
        if l[0] < l[1]:
            return l[0]
        else:
            return l[1]
    rest = find_min(l[1:])
    if l[0] < rest:
        return l[0]
    else:
        return rest

if __name__ == '__main__':
    l = [11,2,3,4,45,3,23,21,32,243,2,1,]
    print(find_max(l), find_min(l))