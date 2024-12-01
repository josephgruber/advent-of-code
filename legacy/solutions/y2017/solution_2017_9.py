import sys, os
sys.path.insert(0, os.path.dirname(sys.path[0]) + "/.")

from re import sub, findall
from lib.helper import read_input


def garbageCleanupPart1(data):
	data = sub(r"!.", "", data)
	data = sub(r"<[^>]*>", "", data)
	data = sub(r"{,*}", "{}", data)
	return data


def calcGroupScore(data):
	count = 0
	total = 0

	curlyBraces = findall(r"[{}]", data)

	for curlyBrace in curlyBraces:
		if curlyBrace == "{":
			count += 1
		elif curlyBrace == "}":
			total += count
			count -= 1

	return total


def findGroups(data):
	cleanData = garbageCleanupPart1(data)
	groupScore = calcGroupScore(cleanData)

	return groupScore



def garbageCleanupPart2(data):
	total = 0

	data = sub(r"!.", "", data)

	garbage = findall(r"<[^>]*>", data)

	for trash in garbage:
		total += len(trash) - 2

	return total


def main():
	input = read_input("2017_9.txt")
	print("Part 1: " + str(findGroups(input)))
	print("Part 2: " + str(garbageCleanupPart2(input)))


if __name__ == '__main__':
	main()
