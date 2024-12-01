from solutions.y2020.solution_2020_11 import part1, part2

TEST_INPUT = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""


def test_2020_11_1():
    expected_value = 37
    assert part1(TEST_INPUT) == expected_value


def test_2020_11_2():
    expected_value = 26
    assert part2(TEST_INPUT) == expected_value
