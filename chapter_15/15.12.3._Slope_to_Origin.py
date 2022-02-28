import pprint 
from pointClass import Point


def does_it_fails(n, m):
    result = []
    for n,i in enumerate(range(n, m, -1)):
        result.append(float(f'{Point(n+1, i).slope_to_origin():.2f}'))
    return result
        
pprint.pprint(does_it_fails(50, 0))