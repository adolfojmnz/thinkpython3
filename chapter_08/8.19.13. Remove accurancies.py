
import sys

def test(did_pass):
    line_num = sys._getframe(1).f_lineno
    if did_pass:
        print(f'Test at line {line_num} is OK.')
    else: print(f'Test at line {line_num} has FAILED.')

def remove_occurrences(substring, string):
    len_positions = len(find_position(substring, string))
    new_string = ''
    count = 0
    for i in string:
        if string.find(substring) == -1:
            new_string = string
            break
        elif i in substring and count < len(substring)*len_positions:
            count += 1
        else:
            new_string = new_string + i
    return new_string

def find_position(substring, string):
    pos = 0
    st = ''
    while True:
        x = string.find(substring, pos)
        pos += (len(substring) + 1)
        if x == -1:
            break
        st = st + str(x)
    return st

def test_suite():
    test(remove_occurrences("an", "banana") == "ba")
    test(remove_occurrences("cyc", "bicycle") == "bile")
    test(remove_occurrences("iss", "Mississippi") == "Mippi")
    test(remove_occurrences("eggs", "bicycle") == "bicycle")

test_suite()
