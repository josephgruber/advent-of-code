import pytest
import lib.helper


testData = [('AoC 2017', '33efeb34ea91902bb2f59c9920caa6cd'),
            ('', 'a2582a3a0e66e6e86e3812dcb672a272'),
            ('1,2,3', '3efbe78a8d82f29979031a4aa0b16a9d'),
            ('1,2,4', '63960835bcdc130f0b66d7ff4f6a5a8e')]


@pytest.mark.parametrize("input, expected", testData)
def test_knotHash(input, expected):
  assert lib.helper.knot_hash(input) == expected
