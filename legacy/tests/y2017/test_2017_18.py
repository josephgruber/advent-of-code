import pytest
from solutions.y2017.solution_2017_18 import duet


# Part 1
def test_day_18_part_1():
  testData = ('''set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2''', 4)
  assert duet(testData[0]) == testData[1]
