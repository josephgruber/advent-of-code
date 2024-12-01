import sys  # isort:skip
import os  # isort:skip
sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from timeit import default_timer as timer
import networkx as nx
from lib.helper import read_input


def theSumOfItsParts(instructions, laborTime=0):
  graph = nx.DiGraph()

  for step in instructions.splitlines():
    stepComponents = step.strip().split(" ")
    graph.add_edges_from([(stepComponents[1], stepComponents[7])])

  stepOrder = ''.join(nx.lexicographical_topological_sort(graph))

  paths = []
  for path in nx.all_simple_paths(graph, stepOrder[0], stepOrder[-1]):
    pathSum = 0
    for node in path:
      pathSum += ord(node.lower()) - 96 + laborTime
    paths.append(pathSum)

  pathDuration = max(paths)
  if not laborTime:
    pathDuration += 1

  return [stepOrder, pathDuration]


def main():
  data = read_input("2018_7.txt")

  start_time = timer()
  answer = theSumOfItsParts(data, 60)
  end_time = timer()

  print('Part 1: ' + answer[0])
  print('Part 2: ' + str(answer[1]))
  print('Elapsed Time: ' + str(end_time - start_time))


if __name__ == '__main__':
  main()
