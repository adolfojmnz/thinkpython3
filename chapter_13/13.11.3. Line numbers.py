import time 

def multidigits_numberlines(filename):
    lines = open(filename, "r").readlines()
    result = []
    linenum = 0

    for line in lines:
        if line[0] in '0123456789':
            linenum += 1
            result.append(line)
            continue
        linenum += 1
        if len(str(linenum)) == 1:
            zeros = '0000'
        elif len(str(linenum)) == 2:
            zeros = '000'
        elif len(str(linenum)) == 3:
            zeros = '00'
        elif len(str(linenum)) == 4:
            zeros = '0'
        elif len(str(linenum)) == 5:
            zeros = ''
        result.append(f'{zeros}{linenum} ')
        result.append(line)

    return open(filename, "w").write(''.join(result))

t0 = time.time()
multidigits_numberlines('vocab.txt')
t1 = time.time()
print(f'{t1-t0} seconds.')
