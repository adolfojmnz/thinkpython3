f = open("friends.txt", "r")
xs = f.readlines()

xs.sort()

g = open("sorted_friends.txt", "w")
for v in xs:
    g.write(v)
g.close()