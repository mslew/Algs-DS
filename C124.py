def vowel_count(string):
    count = 0
    for char in string:
        if char in "aeiou":
            count += 1
        else:
            continue
    return count

string = "Today was really nice out!"
print(vowel_count(string))