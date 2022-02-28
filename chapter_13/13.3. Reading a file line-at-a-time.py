handle =  open("text.txt", "r")
while True:
    text_line = handle.readline()
    if len(text_line) == 0:
        break
    print(text_line, end="")

handle.close()
