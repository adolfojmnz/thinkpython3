def one_at_the_time(string):
    ix = 0
    while ix < len(string):
        print(string[ix])
        ix += 1
    print('\n')


def one_at_the_time_v2(string):
    for i in string:
        print(i)
    print('\n')

def prefixes_and_subfixes(prefix, subfix, exception, excep_arg):
    l = int(len(exception))
    ct = l
    for i in prefix:
        if exception[abs(l-ct)] == i and ct <= l+1:
            print(i + excep_arg + subfix)
            ct += 1
        else:
            print(i + subfix)


prefixes_and_subfixes('JKLMOPQ', 'ack', 'OQ', 'u')