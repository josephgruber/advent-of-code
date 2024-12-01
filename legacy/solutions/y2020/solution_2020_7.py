import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + '/')  # NOQA: E402

import re  # NOQA: E402
import networkx as nx  # NOQA: E402

from lib.helper import execution_timer, read_input  # pylint: disable=import-error,no-name-in-module # NOQA: E402


def parse_rules(data):
    rules = dict()

    for rule in data.splitlines():
        match = re.match(r'^(.*) bags contain(.*)$', rule)

        if match:
            parent = match.group(1)
            children = match.group(2)

            rules[parent] = dict()

            for child in re.findall(r'([\d]+) (.*?) bag', children):
                rules[parent][child[1]] = child[0]

    return rules


def create_graph(data):
    rules = parse_rules(data)
    graph = nx.DiGraph()

    for rule in rules:
        for child in rules[rule]:
            graph.add_edge(rule, child, count=int(rules[rule][child]))

    return graph


@execution_timer
def part1(data, bag):
    graph = create_graph(data)

    return len(nx.ancestors(graph, bag))


@execution_timer
def part2(data, bag, graph=None):
    total_bags = 0

    if not graph:
        graph = create_graph(data)

    for parent, children in graph[bag].items():
        total_bags += children['count'] + children['count'] * part2(None, parent, graph)

    return total_bags


def main():
    puzzle_input = read_input('2020_7.txt')

    print(f'Part 1: {part1(puzzle_input, "shiny gold")}\n')
    print(f'Part 2: {part2(puzzle_input, "shiny gold")}')


if __name__ == '__main__':
    main()
