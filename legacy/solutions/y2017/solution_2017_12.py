import sys, os
sys.path.insert(0, os.path.dirname(sys.path[0]) + "/.")

from lib.helper import read_input
import networkx as nx


def digitalPlumberPart1(pipes):
	graph = nx.Graph()

	for pipe in pipes.splitlines():
		node, programs = pipe.split(" <-> ")

		for program in programs.split(", "):
			graph.add_edge(int(node), int(program))

	return(len(nx.node_connected_component(graph, 0)))


def digitalPlumberPart2(pipes):
	graph = nx.Graph()

	for pipe in pipes.splitlines():
		node, programs = pipe.split(" <-> ")

		for program in programs.split(", "):
			graph.add_edge(int(node), int(program))

	return(nx.number_connected_components(graph))


def main():
	input = read_input("2017_12.txt")
	print("Part 1 " + str(digitalPlumberPart1(input)))
	print("Part 2: " + str(digitalPlumberPart2(input)))

if __name__ == '__main__':
	main()
