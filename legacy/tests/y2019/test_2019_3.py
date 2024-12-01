import pytest
from solutions.y2019.solution_2019_3 import solution

TEST_DATA_P1 = [('R8,U5,L5,D3\nU7,R6,D4,L4', 6),
                ('R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83', 159),
                ('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7', 135)]

TEST_DATA_P2 = [('R8,U5,L5,D3\nU7,R6,D4,L4', 30),
                ('R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83', 610),
                ('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7', 410)]


@pytest.mark.parametrize('test_input, expected_value', TEST_DATA_P1)
def test_2019_3_1(test_input, expected_value):
  assert solution(test_input)[0] == expected_value


@pytest.mark.parametrize('test_input, expected_value', TEST_DATA_P2)
def test_2019_3_2(test_input, expected_value):
  assert solution(test_input)[1] == expected_value
