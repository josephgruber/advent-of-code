import pytest
from solutions.y2020.solution_2020_10 import part1, part2

TEST_INPUT_P1 = [("""16
10
15
5
1
11
7
19
6
12
4""", 35), ("""28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3""", 220)]

TEST_INPUT_P2 = [("""16
10
15
5
1
11
7
19
6
12
4""", 8), ("""28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3""", 19208)]


@pytest.mark.parametrize('test_input, expected_value', TEST_INPUT_P1)
def test_2020_10_1(test_input, expected_value):
    assert part1(test_input) == expected_value


@pytest.mark.parametrize('test_input, expected_value', TEST_INPUT_P2)
def test_2020_10_2(test_input, expected_value):
    assert part2(test_input) == expected_value
