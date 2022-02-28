def count_letters(string):
    output = {}
    for letter in string.lower():
        if letter != " ":
            output[letter] = output.get(letter, 0) + 1

    output = list(output.items())
    output.sort()
    return output

output = count_letters("ThiS is String with Upper and lower case Letters")
for element in output:
    print(element)
