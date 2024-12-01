import pytest
from solutions.y2017.solution_2017_7 import findRoot, recursiveCircus


# Part 1
def test_day_7_part_1():
  testDataPart1 = [('''pbga (66)
	xhth (57)
	ebii (61)
	havc (66)
	ktlj (57)
	fwft (72) -> ktlj, cntj, xhth
	qoyq (66)
	padx (45) -> pbga, havc, qoyq
	tknk (41) -> ugml, padx, fwft
	jptl (61)
	ugml (68) -> gyxo, ebii, jptl
	gyxo (61)
	cntj (57)''', "tknk")]
  assert findRoot(testDataPart1[0][0]) == testDataPart1[0][1]


# Part 2
def test_day_7_part_2():
  testDataPart2 = [('''pbga (66)
	xhth (57)
	ebii (61)
	havc (66)
	ktlj (57)
	fwft (72) -> ktlj, cntj, xhth
	qoyq (66)
	padx (45) -> pbga, havc, qoyq
	tknk (41) -> ugml, padx, fwft
	jptl (61)
	ugml (68) -> gyxo, ebii, jptl
	gyxo (61)
	cntj (57)''', {"ugml", 60})]

  assert recursiveCircus(testDataPart2[0][0]) == testDataPart2[0][1]
