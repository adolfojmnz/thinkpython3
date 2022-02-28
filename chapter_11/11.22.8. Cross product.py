# u = [a1 b1 c1] ^ v = [a2 b2 c2]
# uxv = [b1c2 - c1b2]i + [c1a2 - a1c2]j + [a1b2 - b1a2]k

def cross_product(u, v):
    a1 = u[0]
    a2 = v[0]

    b1 = u[1]
    b2 = v[1]
    
    c1 = u[2]
    c2 = v[2]
    
    uxv = [b1*c2 - c1*b2, c1*a2 - a1*c2, a1*b2 - b1*a2]
    return uxv
        
print(cross_product([2, 4, -5], [-3, -2, 1]) == [-6, 13, 8])
print(cross_product([1, -3, 4], [-2, 1, 1]) == [-7, -9, -5])
print(cross_product([2, 0, -7], [-3, -4, 0]) == [-28, 21, -8])