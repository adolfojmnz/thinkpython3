f = open("sorted_friends.txt")
content = f.read()
f.close()

words = content.split()
print(f"There are {len(words)} words in the file.")