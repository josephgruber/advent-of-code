import sys, os
sys.path.insert(0, os.path.dirname(sys.path[0]) + "/.")

import networkx as nx
from collections import Counter
from lib.helper import read_input


def findRoot(data):
	subPrograms = set()
	basePrograms = set()

	for programs in data.split("\n"):
		if "->" in programs:
			basePrograms.add(programs.split()[0])
			for program in programs.split(" -> ")[1].split(", "):
				subPrograms.add(program)

	return basePrograms.difference(subPrograms).pop()


def getChildren(node, programs):
	if node in programs:
		for program in programs[node]:
			yield program
			yield from getChildren(program, programs)


def recursiveCircus(data):
	programs, weights, towerWeights = {}, {}, {}

	for line in data.replace(",", "").splitlines():
		values = list(map(str, line.split()))
		weights[values[0].strip()] = int(values[1].strip("()"))

		if len(values) > 2:
			programs[values[0].strip()] = values[3:]

	for program in programs[findRoot(data)]:
		total = weights[program]

		for child in getChildren(program, programs):
			if program == "guuri":
				print(child + " " + str(weights[child]))
			total += weights[child]

		towerWeights[program] = total

	weightDifference = max(towerWeights.values()) - min(towerWeights.values())

	print(towerWeights)
	print()
	print(weightDifference)
	print()

	for tower in towerWeights:
		if Counter(towerWeights.values())[towerWeights[tower]] == 1:
			return {tower, weights[tower]-weightDifference}


def main():
	input = read_input("2017_7.txt")
	print("Part 1: " + findRoot(input))
	print("Part 2: " + str(recursiveCircus(input)))


if __name__ == '__main__':
	main()
