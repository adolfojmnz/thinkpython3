f = open("friends.zip", "rb")
g = open("friends_copy.zip", "wb")

while True:
    buf = f.read(1024)
    if len(buf) == 0:
        break
    g.write(buf)

f.close()
g.close()
