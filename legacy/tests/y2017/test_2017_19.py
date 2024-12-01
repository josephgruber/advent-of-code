import pytest
from solutions.y2017.solution_2017_19 import aSeriesOfTubesPart1, aSeriesOfTubesPart2


# Part 1
def test_day_19_part_1():
  testData = ('''     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ 
''', "ABCDEF")
  assert aSeriesOfTubesPart1(testData[0]) == testData[1]


# Part 2
def test_day_19_part_2():
  testData = ('''     |          
     |  +--+    
     A  |  C    
 F---|--|-E---+ 
     |  |  |  D 
     +B-+  +--+ 
''', 38)
  assert aSeriesOfTubesPart2(testData[0]) == testData[1]
