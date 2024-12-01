import pytest
from solutions.y2016.solution_2016_7 import part1, part2, isAbba, isBab


testData_part1 = [('abba[mnop]qrst', True), ('abcd[bddb]xyyx', False),
                  ('aaaa[qwer]tyui', False), ('ioxxoj[asdfgh]zxcvbn', True)]

testData_part2 = [('aba[bab]xyz', True), ('xyx[xyx]xyx', False), ('aaa[kek]eke', True), ('zazbz[bzb]cdb', True)]

testData_isAbba = [('abba', True), ('ioxxoj', True), ('aaaa', False), ('asdfgh', False)]

testData_isBab = [(['aba'], ['bab'], True), (['xyx'], ['xyx'], False), (['zbz'], ['bzb'], True)]


@pytest.mark.parametrize("input, expected", testData_part1)
def test_2016_7_1(input, expected):
  assert part1(input) == expected


@pytest.mark.parametrize("input, expected", testData_part2)
def test_2016_7_2(input, expected):
  assert part2(input) == expected


@pytest.mark.parametrize("input, expected", testData_isAbba)
def test_2016_7_isAbba(input, expected):
  assert isAbba(input) == expected


@pytest.mark.parametrize("aba, seq, expected", testData_isBab)
def test_2016_7_isBab(aba, seq, expected):
  assert isBab(aba, seq) == expected
