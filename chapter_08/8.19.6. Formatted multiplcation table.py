# Formatted multiplication table 12x12

def table(height, n=1):
    for i in range(1, height + 1):
        print('{0:>{1}}'.
              format(i*n, 4 + len(str(i*height))),
              end='  ')
    print("")

def multi_table(height, m=1):
    for i in range(1, height + 1):
        table(height, i*m)


multi_table(12, 4444) # 12 x 4444 :P
