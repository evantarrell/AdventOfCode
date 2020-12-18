# Advent of Code 2020 - Day 3: Toboggan Trajectory

# Part 1,  Move through the input grid and count the number of trees (# symbols) encountered on the way to the bottom starting in the top left corner
# File has 31 characters per row, 323 rows. This pattern repeats to the right until the bottom has been reached moving 3 right then 1 down

def traverse(grid, xSlope, ySlope):
	width = len(grid[0])
	length = len(grid)
	x = 0
	y = 0
	treeCount = 0

	for y in range(0, length, ySlope):
		if grid[y][x] == '#':
			treeCount += 1
		x += xSlope
		x = x - width if x >= width else x

	return treeCount

terrain = []

with open('input.txt', 'r') as file:
	for line in file:
		terrain.append(line.rstrip())

treeCount = traverse(terrain, 3, 1)

print('Part 1: Found ' + str(treeCount) + ' trees')

# Part 2, Same as part 1 but multiply the resultant number of trees across 5 different slopes
# Slope format is x, y so [3, 1] is 3 right 1 down like in part 1

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
part2Result = 1

for slopePair in slopes:
	part2Result *= traverse(terrain, slopePair[0], slopePair[1])

print('Part 2: Product of treeCounts on each slope = ' + str(part2Result))
