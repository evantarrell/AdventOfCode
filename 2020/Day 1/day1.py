# Advent of Code 2020 - Day 1: Report Repair

# Part 1, read input file of expenses, find the two that sum to 2020 and multiply them
import itertools

expenses = []

with open('input.txt', 'r') as input:
	for line in input:
		expenses.append(int(line.rstrip()))

for a, b in itertools.combinations(expenses, 2):
	if a + b == 2020:
		print('a = ' + str(a) + ', b = ' + str(b) + ', a + b = ' + str(a+b) + ', a * b = ' + str(a*b))

# Part 2, find 3 that sum to 2020 and multiply them
for a, b, c in itertools.combinations(expenses, 3):
	if a + b + c == 2020:
		print('a = ' + str(a) + ', b = ' + str(b) + ', c = ' + str(c) + ', a + b + c = ' + str(a+b+c) + ', a * b * c = ' + str(a*b*c))
