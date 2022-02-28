word = 'hello'
if word < "banana":
    print("Your word, " + word + ", comes before banana.")
elif word > "banana":
    print("Your word, " + word + ", comes after banana.")
else:
    print("Yes, we have no bananas!")


greeting = "Hello, world!"
new_greeting = "J" + greeting[1:]
print(new_greeting)
