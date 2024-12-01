import sys, os
sys.path.insert(0, os.path.dirname(sys.path[0]) + "/.")

from collections import defaultdict
from lib.helper import read_input


def changeDirection(turn, direction):
	if turn == "left":
		direction = (direction - 1) % 4
	elif turn == "right":
		direction = (direction + 1) % 4
	elif turn == "reverse":
		direction = (direction + 2) % 4

	return direction


def move(x, y, direction):
	if direction == 0:
		x += 1
	elif direction == 1:
		y += 1
	elif direction == 2:
		x -= 1
	elif direction == 3:
		y -= 1

	return (x, y)


def createGrid(inputGrid):
	grid = defaultdict(lambda: ".")
	inputGrid = inputGrid.splitlines()
	height = len(inputGrid)
	width = len(inputGrid[0])

	for row in range(height):
		for column in range(width):
			grid[(row-height//2, column-width//2)] = inputGrid[column][row]

	return grid


def sporificaVirusPart1(inputGrid, iterations):
	grid = createGrid(inputGrid)
	direction = 3  # 0-3 = right, down, left, up
	node = (0, 0)
	infections = 0

	for _ in range(iterations):
		if grid[node] == ".":
			direction = changeDirection("left", direction)
			grid[node] = "#"
			infections += 1
		else:
			direction = changeDirection("right", direction)
			grid[node] = "."

		node = move(node[0], node[1], direction)

	return infections


def sporificaVirusPart2(inputGrid, iterations):
	grid = createGrid(inputGrid)
	direction = 3  # 0-3 = right, down, left, up
	node = (0, 0)
	infections = 0

	for _ in range(iterations):
		if grid[node] == ".":
			direction = changeDirection("left", direction)
			grid[node] = "W"
		elif grid[node] == "W":
			grid[node] = "#"
			infections += 1
		elif grid[node] == "#":
			direction = changeDirection("right", direction)
			grid[node] = "F"
		elif grid[node] == "F":
			direction = changeDirection("reverse", direction)
			grid[node] = "."

		node = move(node[0], node[1], direction)

	return infections

def main():
	input = read_input("2017_22.txt")
	print("Part 1: " + str(sporificaVirusPart1(input, 10000)))
	print("Part 2: " + str(sporificaVirusPart2(input, 10000000)))


if __name__ == '__main__':
	main()
