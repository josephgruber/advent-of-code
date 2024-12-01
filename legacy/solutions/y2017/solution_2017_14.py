from lib.helper import knot_hash
import networkx as nx
import sys
import os
sys.path.insert(0, os.path.dirname(sys.path[0]) + "/.")


def diskDefragPart1(key):
  used = 0

  for row in range(128):
    hash = knot_hash("-".join([key, str(row)]))
    binHash = '{:0128b}'.format(int(hash, 16))
    used += binHash.count("1")

  return used


def diskDefragPart2(key):
  grid = []

  for row in range(128):
    hash = knot_hash("-".join([key, str(row)]))
    binHash = '{:0128b}'.format(int(hash, 16))
    grid.append([int(digit) for digit in binHash])

  graph = nx.grid_2d_graph(128, 128)
  for x in range(128):
    for y in range(128):
      if not grid[y][x]:
        graph.remove_node((y, x))

  return len(list(nx.connected_components(graph)))


def main():
  print("Part 1: " + str(diskDefragPart1("jxqlasbh")))
  print("Part 2: " + str(diskDefragPart2("jxqlasbh")))


if __name__ == '__main__':
  main()
