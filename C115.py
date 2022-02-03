def is_unique(list):
    for i in range(len(list)): 
        for num in range(len(list)): 
            if i != num:
                if list[i] == list[num]:
                    return False
    return True
list = [1, 2, 3, 4, 5]
print(is_unique(list))