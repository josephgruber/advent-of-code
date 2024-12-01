import sys, os
sys.path.insert(0, os.path.dirname(sys.path[0]) + "/.")

import numpy as np
from lib.helper import read_input


def createRules(bookOfRules):
	rules = []

	for rule in bookOfRules.splitlines():
		input = list(map(list, rule.split(" => ")[0].split("/")))
		output = list(map(list, rule.split(" => ")[1].split("/")))

		for i in range(4):
			rotation = np.rot90(input, i)
			rot = (rotation.flatten().tolist(), output)
			lr = (np.fliplr(rotation).flatten().tolist(), output)
			ud = (np.flipud(rotation).flatten().tolist(), output)

			if rot not in rules:
				rules.append(rot)
			if lr not in rules:
				rules.append(lr)
			if ud not in rules:
				rules.append(ud)

	return rules



def createBlocks(grid, rows, cols):
	squareSize = int(np.sqrt(len(grid)))

	arr = grid.reshape(squareSize, squareSize)
	height, _ = arr.shape

	return (arr.reshape(height//rows, rows, -1, cols)
									.swapaxes(1, 2)
									.reshape(-1, rows, cols))


def createGrid(blocks, height, width):
	_, rows, cols = blocks.shape

	return (blocks.reshape(height//rows, -1, rows, cols)
									.swapaxes(1, 2)
									.reshape(height, width))


def fractalArt(bookOfRules, iterations):
	grid = np.array(['.', '#', '.', '.', '.', '#', '#', '#', '#'])

	rules = createRules(bookOfRules)

	for _ in range(iterations):
		if len(grid) % 2:  # 3x3
			blocks = createBlocks(grid, 3, 3)
		else:  # 2x2
			blocks = createBlocks(grid, 2, 2)

		enhancedGrid = []

		for block in blocks:
			for rule in rules:
				if block.flatten().tolist() == rule[0]:
					enhancedGrid.append(rule[1])

		length = int(np.sqrt(len(np.array(enhancedGrid).flatten())))
		grid = createGrid(np.array(enhancedGrid), length, length).flatten()

	return grid.flatten().tolist().count("#")


def main():
	input = read_input("2017_21.txt")
	print("Part 1: " + str(fractalArt(input, 5)))
	print("Part 2: " + fractalArt(input, 18))


if __name__ == '__main__':
	main()
