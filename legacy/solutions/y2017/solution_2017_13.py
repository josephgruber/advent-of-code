import sys, os
sys.path.insert(0, os.path.dirname(sys.path[0]) + "/.")

import operator
from collections import defaultdict
from lib.helper import read_input


def packetScannerPart1(data):
	firewall = createDictionary(data)
	severity = 0

	for picosecond in range(max(firewall) + 1):
		if firewall[picosecond][1] == 1:
			severity += picosecond * firewall[picosecond][0]

		firewall = moveLayers(firewall)

	return severity


def moveLayers(firewall):
	operators = [operator.add, operator.sub]

	for layer in firewall:
		if firewall[layer][0] == 0:
			continue

		firewall[layer][1] = operators[firewall[layer][2]](firewall[layer][1], 1)

		if (firewall[layer][0] == firewall[layer][1] or
					(firewall[layer][1] == 1 and firewall[layer][2] == 1)):
				firewall[layer][2] = 1 - firewall[layer][2]

	return firewall


def packetScannerPart2(data):
	firewall = createDictionary(data)

	delay = 0

	while True:
		for layer in firewall:
			if not (delay + layer) % (2 * (firewall[layer][0] - 1)):
				break
		else:
			return delay

		delay += 1


def createDictionary(data):
	layers = defaultdict(lambda: [0, 1, 0])

	for layer in data.splitlines():
		depth, range = list(map(int, layer.split(": ")))
		layers[depth] = [range, 1, 0]

	return layers


def main():
	input = read_input("2017_13.txt")
	print("Part 1: " + str(packetScannerPart1(input)))
	print("Part 2: " + str(packetScannerPart2(input)))

if __name__ == '__main__':
	main()
