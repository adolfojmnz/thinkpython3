#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Adolfo Jimenez
#
# Created:     31/05/2020
# Copyright:   (c) Adolfo Jimenez 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def day_of_week(d):
    if d==0:
        print(d, 'represents the day Sunday')
    elif d==1:
        print(d, 'represents the day Monday')
    elif d==2:
        print(d, 'represents the day Thuesday')
    elif d==3:
        print(d, 'represents the day Wednesday')
    elif d==4:
        print(d, 'represents the day Thursday')
    elif d==5:
        print(d, 'represents the day Friday')
    elif d==6:
        print(d, 'represents the day Saturday')
    else:
        print('The number must be between 0 and 6')

d = int(input('Please enter a number to select a day from of the week'
            '\n 0: Sunday'
            '\n 1: Monday'
            '\n 2: Thuesday'
            '\n 3: Wednesday'
            '\n 4: Thursday'
            '\n 5: Friday'
            '\n 6: Saturday'))
day_of_week(d)
