mylist = []
mylist.clear() # Remove all the elements from the list without deleting the list

mylist.append(5) # Add the argument to end of the list
mylist.append(27)
mylist.append(3)
mylist.append(12)
mylist.append([2, 6]) # Ad the elements as a list inside and at the end of the list

mylist.extend([4, 3, 2, 1]) # Extend the list adding the elements at the end of the list
mylist.index(4) # Find the first match for the index in the list
mylist.reverse() # Reverse the whole list 

mylist.remove([2, 6]) # Remove the index given. It could be a list or just an element
mylist.sort() # Sort the list in ascending order (if reverse are is false)
mylist.sort(reverse = True) # Sort the list in descending order

mylist.pop() # Return and remove the last element of the list (by default)

a = mylist.copy() # Use to assign the list to a new variable with different object references
a.insert(0, 666)

b = a # Assign the list from a to b, but keepping the same object reference
b.insert(0, 777) # Either b and a will be affected 

print(a)
print(b)
print(mylist)
