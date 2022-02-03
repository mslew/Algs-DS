def is_even(k):
    isTrue = True
    for i in range(1, k+1):
        if isTrue == True:
            isTrue = False
        else:
            isTrue = True
    return isTrue
num = 10
if is_even(num) == True:
    decision = "Even"
else:
    decision = "Odd"
print(decision)