import pytest
from solutions.y2018.solution_2018_7 import theSumOfItsParts


def test_day_7_part_1():
  testData = ('''Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.''', 'CABDFE')
  assert theSumOfItsParts(testData[0])[0] == testData[1]


def test_day_7_part_2():
  testData = ('''Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.''', 15)
  assert theSumOfItsParts(testData[0])[1] == testData[1]
