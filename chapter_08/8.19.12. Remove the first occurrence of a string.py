import sys

def test(did_pass):
    line_num = sys._getframe(1).f_lineno
    if did_pass:
        print(f'Test at line {line_num} is OK.')
    else: print(f'Test at line {line_num} has FAILED.')

def remove_occurrences(substring, string):
    new_string = ''
    count = 0
    for i in string:
        if string.find(substring) == -1:
            new_string = string
            break
        elif i in substring and count < len(substring):
            count += 1
        else:
            new_string = new_string + i
    return new_string

def test_suite():
    test(remove_occurrences("an", "banana") == "bana")
    test(remove_occurrences("cyc", "bicycle") == "bile")
    test(remove_occurrences("iss", "Mississippi") == "Missippi")
    test(remove_occurrences("eggs", "bicycle") == "bicycle")

test_suite()
