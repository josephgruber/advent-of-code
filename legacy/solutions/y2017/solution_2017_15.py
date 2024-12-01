from itertools import islice


def duelingGeneratorPart1(generatorA, generatorB):
	total = 0

	for _ in range(40000000):
		generatorA = (generatorA * 16807) % 2147483647
		generatorB = (generatorB * 48271) % 2147483647
		binGeneratorA = "{0:032b}".format(generatorA)
		binGeneratorB = "{0:032b}".format(generatorB)

		if binGeneratorA[16:] == binGeneratorB[16:]:
			total += 1

	return total


def generator(start, factor, multiple):
	value = start

	while True:
		value = (value * factor) % 2147483647
		if value % multiple == 0:
			yield value


def duelingGeneratorPart2(aStart, bStart, aMultiple, bMultiple):
	aGenerator = generator(aStart, 16807, aMultiple)
	bGenerator = generator(bStart, 48271, bMultiple)

	return sum(a % 65536 == b % 65536 for a, b
												in islice(zip(aGenerator, bGenerator), 5000000))


def main():
	print("Part 1: " + str(duelingGeneratorPart1(783, 325)))
	print("Part 2: " + str(duelingGeneratorPart2(783, 325, 4, 8)))


if __name__ == '__main__':
	main()
