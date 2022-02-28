def remove_vowels(s):
    vowels = "aeiouAEIOU"
    s_sans_vowels = ""
    for x in s:
        if not x in vowels:
            s_sans_vowels += x
            #print(s_sans_vowels)
    return s_sans_vowels

print(remove_vowels('Hello, word!'))