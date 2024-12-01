import pytest
from solutions.y2018.solution_2018_12 import subterraneanSustainability


def test_day_12_part_1():
  testData = ('''initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #''', 325)
  assert subterraneanSustainability(testData[0], 20) == testData[1]
