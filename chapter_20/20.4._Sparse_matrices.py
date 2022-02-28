matrixx = [
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0],
        ]
print(matrixx[0][3])
print(matrixx[3][3])

matrix = {(0, 3): 1, (1, 2): 2, (4, 3): 3} 
print(matrix.get((0, 3), 0))
print(matrix.get((3, 3), 0))

