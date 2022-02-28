from unit_tester import test

def remove_occurs(old, new, string):
    result = ''
    for i, ch in enumerate(string):
        if string[i] == old:
            if string[i+1] == old:
                continue
        result += ch
    return new.join(result.split(old))


test(remove_occurs(" ", "**", "Words will now      be  separated by stars."))
test(remove_occurs(",", ";", "this, that, and some other thing")
    == "this; that; and some other thing")
