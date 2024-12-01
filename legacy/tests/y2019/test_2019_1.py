from solutions.y2019.solution_2019_1 import solution


def test_2019_1_1():
  test_input = '12\n14\n1969\n100756'
  expected_value = 34241
  arg_1 = False

  assert solution(test_input, arg_1) == expected_value


def test_2019_1_2():
  test_input = '14\n1969\n100756'
  expected_value = 51314
  arg_1 = True

  assert solution(test_input, arg_1) == expected_value
