layout = "{0:>4}{1:>6}{2:>6}{3:>8}{4:>13}{5:>23}"

print(layout.format("i", "i**2", "i**3", "i**5", "i**10", "i**20"))
for i in range(1, 11):
    print(layout.format(i, i**2, i**3, i**5, i**10, i**20))