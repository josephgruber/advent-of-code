import pytest
from solutions.y2018.solution_2018_2 import invMgmtSystemPart1, invMgmtSystemPart2


# Part 1
def test_day_2_part_1():
  testData = ('''abcdef
bababc
abbcde
abcccd
aabcdd
abcdee
ababab''', 12)
  assert invMgmtSystemPart1(testData[0]) == testData[1]


# Part 2
def test_day_2_part_2():
  testData = ('''abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz''', 'fgij')
  assert invMgmtSystemPart2(testData[0]) == testData[1]
