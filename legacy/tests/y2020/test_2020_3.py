from solutions.y2020.solution_2020_3 import check_slope, all_slopes


TEST_INPUT = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""


def test_2020_3_1():
    slope = (3, 1)
    expected_value = 7

    assert check_slope(TEST_INPUT, slope) == expected_value


def test_2020_3_2():
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    expected_value = 336

    assert all_slopes(TEST_INPUT, slopes) == expected_value
