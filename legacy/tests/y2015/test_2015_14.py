import pytest
from solutions.y2015.solution_2015_14 import reindeerOlympics


def test_day_14_part_1():
  testData = ('''Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.''', 1000, 1120)
  assert reindeerOlympics(testData[0], testData[1]) == testData[2]
