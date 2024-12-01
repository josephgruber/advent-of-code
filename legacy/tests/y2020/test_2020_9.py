from solutions.y2020.solution_2020_9 import part1, part2

TEST_INPUT = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


def test_2020_9_1():
    preamble_length = 5
    expected_value = 127

    assert part1(TEST_INPUT, preamble_length=preamble_length) == expected_value


def test_2020_9_2():
    preamble_length = 5
    expected_value = 62

    target = part1(TEST_INPUT, preamble_length=preamble_length)

    assert part2(TEST_INPUT, target=target) == expected_value
