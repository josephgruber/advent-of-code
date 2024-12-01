def redistributionCyclesPart1(data):
	memoryBanks = list(map(int, data.split()))
	states = []

	while len(states) == len(set(states)):
		states.append(''.join(map(str, memoryBanks)))
		index = memoryBanks.index(max(memoryBanks))
		value = memoryBanks[index]

		memoryBanks[index] = 0
		index += 1

		while value > 0:
			if index == len(memoryBanks):
				index = 0
			memoryBanks[index] += 1
			index += 1
			value -= 1

	return len(set(states))


def redistributionCyclesPart2(data):
	memoryBanks = list(map(int, data.split()))
	states = []

	while len(states) == len(set(states)):
		states.append(''.join(map(str, memoryBanks)))
		index = memoryBanks.index(max(memoryBanks))
		value = memoryBanks[index]

		memoryBanks[index] = 0
		index += 1

		while value > 0:
			if index == len(memoryBanks):
				index = 0
			memoryBanks[index] += 1
			index += 1
			value -= 1

	return len(states) - states.index(''.join(map(str, memoryBanks)))


def main():
	input = "11	11	13	7	0	15	5	5	4	4	1	1	7	1	15	11"
	print("Part 1: " + str(redistributionCyclesPart1(input)))
	print("Part 2: " + str(redistributionCyclesPart2(input)))



if __name__ == '__main__':
	main()
