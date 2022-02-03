l1 = [2, 5, 7, 4, 6, 9, 8]
l2 = [1, 5, 3, 2, 8, 10, 11]
l3 = [12, 11, 13, 1, 5, 3, 7]
l1.sort()
l2.sort()
l3.sort()
count =  0
i = 0
for num in l1:
    if l1[i] == l2[i] == l3[i]:
        count += 1
    else:
        continue 
    i += 1
print(count)

#log(n) for sorting and n for loop
