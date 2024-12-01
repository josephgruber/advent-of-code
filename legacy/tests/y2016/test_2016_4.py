import pytest
from solutions.y2016.solution_2016_4 import solution, isRealRoom, decrypt


testData_isRealRoom = [('aaaaa-bbb-z-y-x-', 'abxyz', True), ('a-b-c-d-e-f-g-h-', 'abcde', True),
                       ('not-a-real-room-', 'oarel', True), ('totally-real-room-', 'decoy', False)]


def test_2016_4():
  input = '''aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]'''
  expected = 1514
  assert solution(input)[0] == expected


@pytest.mark.parametrize("room, checksum, expected", testData_isRealRoom)
def test_2016_4_isRealRoom(room, checksum, expected):
  assert isRealRoom(room, checksum) == expected


def test_2016_4_decrypt():
  room = 'qzmt-zixmtkozy-ivhz-'
  sector = 343
  expected = 'very encrypted name'
  assert decrypt(room, sector) == expected
