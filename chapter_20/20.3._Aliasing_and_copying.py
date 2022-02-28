opposites = {"up": "down", "right": "wrong", "yes": "no"}

alias = opposites
copy = opposites.copy()         # shallow copy

alias["right"] = "left"
copy["right"] = "privilege"

print(opposites["right"])
print(copy["right"])

