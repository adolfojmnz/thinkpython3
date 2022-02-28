def count_letters(fruit, ch):
    count = 0
    for char in fruit:
        if char == ch:
            count += 1
    print(count)

count_letters('banana', 'a')

def count_letters_v2(string, substring): # Capable of counting multiple characters substring
    start, count = 0, 0
    for i in range(0, len(string), len(substring)):
        if string.find(substring, start) != -1:
            count += 1
        start += len(substring)
    return count

print(count_letters_v2('banana', 'an'))