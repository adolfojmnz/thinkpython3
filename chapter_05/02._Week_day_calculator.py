def week_days_calculator():
    return int(td % 7)
    

n = int(input('In which day of the week are you planning to leave'
            '\n 0: Sunday'
            '\n 1: Monday'
            '\n 2: Thuesday'
            '\n 3: Wednesday'
            '\n 4: Thursday'
            '\n 5: Friday'
            '\n 6: Saturday'
            '\n R: '))
td = int(input('\n how many days do yo plan to spend there?'
               '\n R: '))

Final_day = week_days_calculator()

if Final_day == 0:
    print('You will return on a sunday')
if Final_day == 1:
    print('You will return on a monday')
if Final_day == 2:
    print('You will return on a thuesday')
if Final_day == 3:
    print('You will return on a wednesday')
if Final_day == 4:
    print('You will return on a thursday')
if Final_day == 5:
    print('You will return on a friday')
if Final_day == 6:
    print('You will return on a saturday')
