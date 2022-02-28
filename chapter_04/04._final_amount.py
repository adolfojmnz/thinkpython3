#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Adolfo Jimenez
#
# Created:     28/05/2020
# Copyright:   (c) Adolfo Jimenez 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def final_amt(p, r, n, t):
    """
        Apply the compund interest formula to p
        to produce the final amount
    """
    a = p * (1 + (r/n) ) ** (n*t)
    return a

toInvest = float(input('How much do you want to invest'))
fnl = final_amt(toInvest, 0.08, 12, 5)
print('At the and of the peirod you will have', fnl)