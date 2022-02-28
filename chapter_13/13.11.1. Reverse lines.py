def reverse_lines(filename, newfile):	# I don't like this one.
    result = []
    for i in open(filename).readlines():
    	result.insert(0, i)
    result = ''.join(result)
    open(newfile, 'w').write(result)


def reverse_lines_(filename):			# This is a much efficient version. I do like this one.
	_file_lines = open(filename).readlines()
	_file_lines.reverse()
	open(filename, 'w').write(''.join(_file_lines))	# Delete the exintent text and write the new reversed one. 

def read_file(filename):				# Print the text into the file. 
	return ''.join(open(filename).readlines())


#print(read_file("newfile.txt"))
reverse_lines_("example2.txt")
