# Advent of Code 2020 - Day 2: Password Philosophy

# Part 1, read input file with each line containing the password policy and password. Find how many passwords are valid based on their policies
# Ex: 1-3 a: abcde is valid as there is 1 a in abcde
# but 3-7 l: ablleiso is not valid as there are only 2 l's in ablleiso

import re

regexPattern = '(\\d+)-(\\d+) (\\w): (\\w+)'
validPasswordCount = 0

with open('input.txt', 'r') as input:
	for line in input:
		match = re.search(regexPattern, line)
		
		if match is not None:
			lowerLimit = int(match.group(1))
			upperLimit = int(match.group(2))
			letter = match.group(3)
			password = match.group(4)

			letterCount = password.count(letter)

			if letterCount >= lowerLimit and letterCount <= upperLimit:
				validPasswordCount += 1

print('Part 1: There were ' + str(validPasswordCount) + ' valid passwords')

# Part 2, same but the password policy meaning is different.
# Instead of counts it denotes two positions for the given letter to occur in, base 1 indexing. The letter must occur in exactly one of the two positions, other occurrences don't matter

validPasswordCount = 0

with open('input.txt', 'r') as input:
	for line in input:
		match = re.search(regexPattern, line)
		
		if match is not None:
			pos1 = int(match.group(1)) - 1
			pos2 = int(match.group(2)) - 1
			letter = match.group(3)
			password = match.group(4)

			if len(password) > pos2 and (password[pos1] == letter or password[pos2] == letter) and not (password[pos1] == password[pos2]):
				validPasswordCount += 1

print('Part 2: There were ' + str(validPasswordCount) + ' valid passwords')
