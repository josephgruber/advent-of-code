import sys  # isort:skip
import os  # isort:skip
sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from collections import defaultdict
from timeit import default_timer as timer
from lib.helper import read_input


def reposeRecordPart1(input):
  guards, sleepRecords = parseSleepRecords(input)

  sleepiestGuard = max(guards, key=guards.get)
  maxSleep = 1

  for sleepRecord, sleepRepeatTimes in sleepRecords.items():
    if sleepRecord[0] == sleepiestGuard:
      if sleepRepeatTimes > maxSleep:
        maxSleep = sleepRepeatTimes
        maxSleepTime = sleepRecord[1]

  return sleepiestGuard * maxSleepTime


def reposeRecordPart2(input):
  _guards, sleepRecords = parseSleepRecords(input)

  maxSleep = 1

  for sleepRecord, sleepRepeatTimes in sleepRecords.items():
    if sleepRepeatTimes > maxSleep:
      maxSleep = sleepRepeatTimes
      maxSleepTime = sleepRecord[1]
      maxSleepGuard = sleepRecord[0]

  return maxSleepGuard * maxSleepTime


def parseSleepRecords(input):
  guards = defaultdict(int)
  sleepRecords = defaultdict(int)

  for record in sorted(input.splitlines()):
    if 'begins shift' in record:
      guardId = int(record.split()[3][1:].strip())
    elif 'falls asleep' in record:
      asleep = int(record.split()[1][3:5])
    elif 'wakes up' in record:
      awake = int(record.split()[1][3:5])
      guards[guardId] += (awake - asleep)

      for minute in range(asleep, awake):
        sleepRecords[(guardId, minute)] += 1

  return guards, sleepRecords


def main():
  data = read_input("2018_4.txt")

  start_time = timer()
  print("Part 1: " + str(reposeRecordPart1(data)))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))
  print()

  start_time = timer()
  print("Part 2: " + str(reposeRecordPart2(data)))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))


if __name__ == '__main__':
  main()
