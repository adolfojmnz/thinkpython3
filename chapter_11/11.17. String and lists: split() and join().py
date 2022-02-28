song = "The rain in the woods is like the rain in air, unpredictible..."
wds = song.split()

glue = 'winter'
result = glue.join(song.split('rain'))
print(result)
print(song.split('rain'))
# The split method convert the string into a list which elements are divided 
# when the argument given to the method is found.