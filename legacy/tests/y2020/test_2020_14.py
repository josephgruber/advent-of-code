from solutions.y2020.solution_2020_14 import part1, part2


def test_2020_14_1():
    test_input = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""
    expected_value = 165

    assert part1(test_input) == expected_value


def test_2020_14_2():
    test_input = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""
    expected_value = 208

    assert part2(test_input) == expected_value
