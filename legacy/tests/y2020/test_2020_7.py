import pytest
from solutions.y2020.solution_2020_7 import part1, part2

TEST_INPUT_P1 = [('''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.''', 4)]

TEST_INPUT_P2 = [('''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.''', 32), ('''shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.''', 126)]


@pytest.mark.parametrize('test_input, expected_value', TEST_INPUT_P1)
def test_2020_7_1(test_input, expected_value):
    bag_type = 'shiny gold'
    expected_value = 4

    assert part1(test_input, bag_type) == expected_value


@pytest.mark.parametrize('test_input, expected_value', TEST_INPUT_P2)
def test_2020_7_2_case1(test_input, expected_value):
    bag_type = 'shiny gold'

    assert part2(test_input, bag_type) == expected_value
