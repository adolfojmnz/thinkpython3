inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}

def del_item(item, dictionary):
    if item != "":
        del dictionary[item]
        return dictionary
    return "Nothing to delete" 

print('apples' in inventory.values())
print('apples' in inventory.keys())

