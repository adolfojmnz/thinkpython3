def snake_lines(filename, string):
	result = []
	for line in open(filename).readlines():
		if string in line:
			result.append(line)
	return ''.join(result)

print(snake_lines('example2.txt', 'Hello'))
