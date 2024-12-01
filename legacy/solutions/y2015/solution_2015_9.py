import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from timeit import default_timer as timer
import networkx as nx
from lib.helper import read_input


def allInASingleNight(routes):
  graph = nx.Graph()

  for route in routes.splitlines():
    nodes, distance = route.strip().split(' = ')
    nodes = nodes.split(' to ')

    graph.add_nodes_from(nodes)
    graph.add_edge(nodes[0], nodes[1], distance=int(distance))

  pathLengths = list()
  nodeCount = len(graph.nodes)

  for circuit in nx.eulerian_circuit(nx.eulerize(graph)):
    for path in nx.all_simple_paths(G=graph, source=circuit[0], target=circuit[1]):
      if len(path) < nodeCount:
        continue

      pathLengths.append(sum(graph[path[i]][path[i + 1]]['distance'] for i in range(len(path) - 1)))

  return (min(pathLengths), max(pathLengths))


def main():
  data = read_input("2015_9.txt")

  start_time = timer()
  results = allInASingleNight(data)
  end_time = timer()

  print('Part 1: ' + str(results[0]))
  print('Part 2: ' + str(results[1]))
  print('Elapsed Time: ' + str(end_time - start_time))


if __name__ == '__main__':
  main()
