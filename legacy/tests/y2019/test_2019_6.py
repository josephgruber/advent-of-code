from solutions.y2019.solution_2019_6 import part_1, part_2


def test_2019_6_1():
  test_input = '''COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L'''
  expected_value = 42
  assert part_1(test_input) == expected_value


def test_2019_6_2():
  test_input = '''COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN'''
  expected_value = 4
  parameter_a = 'YOU'
  parameter_b = 'SAN'
  assert part_2(test_input, parameter_a, parameter_b) == expected_value
