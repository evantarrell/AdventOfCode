def splitList(list, direction):
	length = int(len(list) / 2)
	if direction == 'lower':
		halfList = list[:length]
	else:
		halfList = list[length:]

	return halfList

foundSeats = []

with open('input.txt', 'r') as file:
	for line in file:
		rows = list(range(0, 128))
		cols = list(range(0, 8))

		for char in line:
			if char == 'F' or char == 'B':
				rows = splitList(rows, 'lower' if char == 'F' else 'upper')
			elif char == 'L' or char == 'R':
				cols = splitList(cols, 'lower' if char == 'L' else 'upper')

		foundSeats.append(rows[0] * 8 + cols[0])

print('Part 1: Largest seat ID is', max(foundSeats))

expectedSeats = list(range(min(foundSeats), max(foundSeats) + 1))

santasSeat = [seat for seat in expectedSeats if seat not in foundSeats][0]

print('Part 2: Santa\'s seat is seat ID', santasSeat)