# Now rewrite the count_letters function so that instead of traversing the string,
# it repeatedly calls the find method, with the optional third parameter to locate
# new occurrences of the letter being counted.

def count_letters_v2(fruit, ch):
    pos = 0
    count = ''
    while fruit.find(ch, pos) != -1:
        count = count + str(fruit.find(ch, pos))    #print(count)
        pos = 1 + fruit.find(ch, pos)
    print(len(count))

count_letters_v2('banana', 'an')