from solutions.y2020.solution_2020_1 import part1, part2


def test_2020_1_1():
    test_input = test_input = '1721\n979\n366\n299\n675\n1456'
    expected_value = 514579

    assert part1(test_input) == expected_value


def test_2020_1_2():
    test_input = '1721\n979\n366\n299\n675\n1456'
    expected_value = 241861950

    assert part2(test_input) == expected_value
