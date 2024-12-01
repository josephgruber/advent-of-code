import pytest
from solutions.y2015.solution_2015_9 import allInASingleNight

testData = ['''London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141''', 605, 982]


def test_2015_9_1():
  assert allInASingleNight(testData[0])[0] == testData[1]


def test_2015_9_2():
  assert allInASingleNight(testData[0])[1] == testData[2]
