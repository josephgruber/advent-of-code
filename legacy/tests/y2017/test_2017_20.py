import pytest
from solutions.y2017.solution_2017_20 import particleSwarm


# Part 1
def test_day_20_part_1():
  testData = ('''p=<3,0,0>, v=<2,0,0>, a=<-1,0,0>
p=<4,0,0>, v=<0,0,0>, a=<-2,0,0>''', 0)
  assert particleSwarm(testData[0]) == testData[1]
