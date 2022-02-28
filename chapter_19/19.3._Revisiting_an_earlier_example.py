def recursion_depth(number):

    print(f'Recursion depth numer: {number}')
    try:
        recursion_depth(number+ 1)
    except:
        print('Going deeper inside the wormhole is not possible')

recursion_depth(0)
