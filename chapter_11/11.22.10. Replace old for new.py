
def replace(text, old, new):
	return new.join(text.split(old))
    
s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
print(replace("Mississippi", "i", "I") == 'MIssIssIppI')
print(replace(s, "o", "a") == "I lave spam! Spam is my favarite faad. Spam, spam, yum!")
print(replace(s, "om", "am") == "I love spam! Spam is my favorite food. Spam, spam, yum!")
print(replace('74367', '7', '8') == '84368')