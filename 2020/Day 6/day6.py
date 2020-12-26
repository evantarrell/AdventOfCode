groups = []

with open('input.txt', 'r') as file:
	group = ''
	for line in file:
		if line != '\n':
			group += line
		else:
			groups.append(group.replace('\n', ' '))
			group = ''

	if group != '':
		groups.append(group.replace('\n', ' '))

total = 0

for group in groups:
	uniqueLetters = set(group)
	if ' ' in uniqueLetters:
		uniqueLetters.remove(' ')
	total += len(uniqueLetters)

print('Part 1:', total)

total = 0

for group in groups:
	a = group.split(' ')
	if '' in a:
		a.remove('')
	
	responseSets = []

	for response in a:
		responseSets.append(set(response))

	intersection = set.intersection(*responseSets)

	if intersection != set():
		total += len(intersection)

print('Part 2:', total)
