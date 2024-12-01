from solutions.y2022.solution_2022_5 import part1, part2

TEST_INPUT = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""


def test_2022_5_1():
    expected_value = 'CMZ'

    assert part1(TEST_INPUT) == expected_value


def test_2022_5_2():
    expected_value = 'MCD'
    assert part2(TEST_INPUT) == expected_value
