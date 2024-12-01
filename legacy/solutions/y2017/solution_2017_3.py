from collections import defaultdict


def spiralGridPart1(data):
	x, y = 0, 0
	steps, value = 1, 1
	grid = {(x, y): value}
	directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Right, Up, Left, Down

	while value <= data:
		for move in range(4):
			for _ in range(steps):
				value += 1

				x = x + directions[move][0]
				y = y + directions[move][1]

				grid[x, y] = value

			if move % 2:
				steps += 1
	return grid


def spiralGridPart2(data):
	x, y = 0, 0
	steps, value = 1, 1
	grid = defaultdict(int)
	grid[x, y] = value
	directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Right, Up, Left, Down

	while True:
		for move in range(4):
			for _ in range(steps):
				x = x + directions[move][0]
				y = y + directions[move][1]

				grid[x, y] = calculateValue(x, y, grid)
				maxValue = grid[x, y]
				if grid[x, y] > data:
					return maxValue

			if move % 2:
				steps += 1


def manhattanDistance(data):
	grid = spiralGridPart1(data)

	distance = list(grid.keys())[list(grid.values()).index(data)]

	return abs(distance[0]) + abs(distance[1])


def calculateValue(posX, posY, grid):
	adjacent = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
	value = 0

	for move in range(8):
		adjacentX = posX + adjacent[move][0]
		adjacentY = posY + adjacent[move][1]
		value += grid[adjacentX, adjacentY]

	return value


def main():
	input = 265149
	print("Part 1: " + str(manhattanDistance(input)))
	print("Part 2: " + str(spiralGridPart2(input)))


if __name__ == '__main__':
	main()
