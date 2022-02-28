#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Adolfo Jimenez
#
# Created:     01/06/2020
# Copyright:   (c) Adolfo Jimenez 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

xg = [83,75,74.9,70,69.9,65,60,59.9,55,50,49.9,45,44.9,40,39.9,2,0]
for v in xg:
    if v > 75:
       print(v, 'First')
    elif v>=70 and v<75:
         print(v, 'Upper Second')
    elif v>=60 and v<70:
         print(v, 'Second')
    elif v>=50 and v<60:
         print(v, 'Third')
    elif v>=45 and v<50:
         print(v, 'F1 Supp')
    elif v>=40 and v<45:
         print(v, 'F2')
    elif v<40:
         print(v, 'F3')