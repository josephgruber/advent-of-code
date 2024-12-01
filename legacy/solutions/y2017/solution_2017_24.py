import sys, os
sys.path.insert(0, os.path.dirname(sys.path[0]) + "/.")

from lib.helper import read_input


def createBridges(bridge, components):
	matches = [component for component in components if bridge[1] in component]

	if not len(matches):
		yield (bridge[0], sum(sum(ports) for ports in bridge[0]), len(bridge[0]))
	else:
		for component in matches:
			components_ = components.copy()
			components_.remove(component)

			for bridge_ in createBridges((bridge[0] + [component], component[0] if bridge[1] == component[1] else component[1]), components_):
				yield bridge_

def electromagneticMoatPart1(data):
	components = [tuple(map(int, line.split("/"))) for line in data.splitlines()]

	bridges = createBridges(([], 0), components)

	return max(bridge[1] for bridge in bridges)


def electromagneticMoatPart2(data):
	components = [tuple(map(int, line.split("/"))) for line in data.splitlines()]

	bridges = list(createBridges(([], 0), components))

	maxLength = max(bridge[2] for bridge in bridges)

	return max(bridge[1] for bridge in bridges if bridge[2] == maxLength)


def main():
	input = read_input("2017_24.txt")
	print("Part 1: " + str(electromagneticMoatPart1(input)))
	print("Part 2: " + str(electromagneticMoatPart2(input)))


if __name__ == '__main__':
	main()
