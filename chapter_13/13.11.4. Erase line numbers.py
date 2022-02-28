import time 

def __erase_line_numbers(filename):
    
    lines = open(filename, "r").readlines()
    first_line = open(filename, "r").readline()
    lenght = len(str(first_line.split()[0])) + 1
    result = []

    for line in lines:
        if str(line[0]) in '0123456789':
            result.append(line[lenght:])
        else: 
            result.append(line)
    return open(filename, "w").write(''.join(result))

t0 = time.time()
__erase_line_numbers('vocab.txt')
t1 = time.time()
print(f'{t1-t0} seconds.')
