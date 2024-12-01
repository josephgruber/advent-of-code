import pytest
from solutions.y2017.solution_2017_9 import findGroups, calcGroupScore, garbageCleanupPart1, garbageCleanupPart2

# Part 1
testData = [("{}", 1),
            ("{{{}}}", 6),
            ("{{},{}}", 5), ("{{{},{},{{}}}}", 16),
            ("{<a>,<a>,<a>,<a>}", 1),
            ("{{<ab>},{<ab>},{<ab>},{<ab>}}", 9),
            ("{{<!!>},{<!!>},{<!!>},{<!!>}}", 9),
            ("{{<a!>},{<a!>},{<a!>},{<ab>}}", 3)]


@pytest.mark.parametrize("input, expected", testData)
def test_day_9_part_1_findGroups(input, expected):
  assert findGroups(input) == expected


testData = [("{}", 1),
            ("{{}}", 3),
            ("{{{},{},{{}}}}", 16),
            ("{{},{},{},{}}", 9)]


@pytest.mark.parametrize("input, expected", testData)
def test_day_9_part_1_calcGroupScore(input, expected):
  assert calcGroupScore(input) == expected


testData = [("{}", "{}"),
            ("{{{}}}", "{{{}}}"),
            ("{{},{}}", "{{},{}}"),
            ("{{{},{},{{}}}}", "{{{},{},{{}}}}"),
            ("{<{},{},{{}}>}", "{}"),
            ("{<a>,<a>,<a>,<a>}", "{}"),
            ("{{<a>},{<a>},{<a>},{<a>}}", "{{},{},{},{}}"),
            ("{{<!>},{<!>},{<!>},{<a>}}", "{{}}")]


@pytest.mark.parametrize("input, expected", testData)
def test_day_9_part_1_garbageCleanup(input, expected):
  assert garbageCleanupPart1(input) == expected


# Part 2
testData = [('<>', 0), ('<random characters>', 17),
            ('<<<<>', 3), ('<{!>}>', 2), ('<!!>', 0),
            ('<!!!>>', 0), ('<{o"i!a,<{i<a>', 10)]


@pytest.mark.parametrize("input, expected", testData)
def test_day_9_part_2(input, expected):
  assert garbageCleanupPart2(input) == expected
