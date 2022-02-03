def word_count(string):
    bigList = dict()
    for word in string.lower().split():
        if word in bigList:
            bigList[word] += 1
        else:
            bigList[word] = 1

    return bigList 

string = "I really need to get some sleep. I need to get my homework done also"
print(word_count(string))