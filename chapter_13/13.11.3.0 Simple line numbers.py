def add_ln(filename):
    result = []
    linenum = 0
    lines = open(filename, "r").readlines()
    for line in lines:
        linenum += 1
        if line[0] not in '0123456789':
            result.append(str(linenum))
            result.append(' ')
            result.append(line)
        else:
            result.append(line)
    open(filename, "w").write('')
    return open(filename, "w").write(''.join(result))


add_ln('line_numbers.txt')
