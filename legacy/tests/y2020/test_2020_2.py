from solutions.y2020.solution_2020_2 import part1, part2


def test_2020_2_1():
    test_input = '1-3 a: abcde\n1-3 b: cdefg\n2-9 c: ccccccccc'
    expected_value = 2

    assert part1(test_input) == expected_value


def test_2020_2_2():
    test_input = '1-3 a: abcde\n1-3 b: cdefg\n2-9 c: ccccccccc'
    expected_value = 1

    assert part2(test_input) == expected_value
