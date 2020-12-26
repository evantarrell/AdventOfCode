import re

rules = {}
regex = '(\\d+)? ?(\\w+ \\w+) bags?'
startingBag = 'shiny gold'

with open('input.txt', 'r') as file:
	for line in file:
		matches = re.findall(regex, line)
		if matches:
			rules[matches[0][1]] = matches[1:]

bagLayers = []
prevLayer = []
newLayer = [startingBag]

while newLayer:
	prevLayer = newLayer
	newLayer = []

	for rule in rules:
		if any(bag in prevLayer for qty, bag in rules[rule]):
			newLayer.append(rule)

	if newLayer:
		for bag in newLayer:
			if bag not in bagLayers:
				bagLayers.append(bag)

print('Part 1:', len(bagLayers), 'bags can hold a shiny gold bag')

class Bag:
	def __init__(self, color='', qty=0):
		self.color = color
		self.qty = qty
		self.children = []

	def numContainedBags(self):
		return sum(bag.qty + bag.numContainedBags() * bag.qty for bag in self.children)

startingBag = Bag('shiny gold', 1)

bagList = [startingBag]

while bagList:
	newList = []

	for bag in bagList:
		for qty, color in rules[bag.color]:
			if color != 'no other':
				childBag = Bag(color, int(qty))
				bag.children.append(childBag)

		newList.extend(bag.children)

	bagList = newList

print('Part 2: The shiny gold bag must contain', startingBag.numContainedBags(), 'bags')
