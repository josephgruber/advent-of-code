import sys, os
sys.path.insert(0, os.path.dirname(sys.path[0]) + "/.")

from lib.helper import read_input


def parse(buffer):
	particles = []

	for particle in buffer.splitlines():
		particles.append([list(map(int, poscoord[3:-1].split(",")))
																				for poscoord in particle.split(", ")])

	return particles


def calculateCoordinates(coordinates):
	return sum(abs(coordinate) for coordinate in coordinates)


def particleSwarm(buffer):
	particles = parse(buffer)
	acceleration, velocity, position = [], [], []

	for particle in particles:
		position.append(calculateCoordinates(particle[0]))
		velocity.append(calculateCoordinates(particle[1]))
		acceleration.append(calculateCoordinates(particle[2]))

	lowestAcceleration = [index for index, val in enumerate(acceleration) if val == min(acceleration)]

	return lowestAcceleration[0]


def main():
	input = read_input("2017_20.txt")
	print("Part 1: " + str(particleSwarm(input)))


if __name__ == '__main__':
	main()
