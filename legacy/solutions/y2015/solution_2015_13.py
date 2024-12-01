import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from itertools import permutations
from timeit import default_timer as timer
from lib.helper import read_input


def knightsOfTheDinnerTable(attendeesList):
  happinessLevels = dict()
  attendees = set()
  maxHappiness = 0

  for attendee in attendeesList.splitlines():
    data = attendee.strip().split(' ')
    attendeeA = data[0]
    attendeeB = data[-1].strip('.')

    if data[2] == 'gain':
      happinessLevels[(attendeeA, attendeeB)] = int(data[3])
    else:
      happinessLevels[(attendeeA, attendeeB)] = int(data[3]) * -1

    attendees.update([attendeeA, attendeeB])

  for seatingChart in permutations(attendees):
    seatingChart = seatingChart + (seatingChart[0],)
    totalHappiness = 0

    for i in range(len(seatingChart) - 1):
      totalHappiness += happinessLevels[(seatingChart[i], seatingChart[i + 1])] + \
          happinessLevels[(seatingChart[i + 1], seatingChart[i])]

    if totalHappiness > maxHappiness:
      maxHappiness = totalHappiness

  return maxHappiness


def addMe(attendeesList):
  for attendee in set([attendee.split(' ')[0] for attendee in attendeesList.splitlines()]):
    attendeesList += 'Me would gain 0 happiness units by sitting next to ' + attendee + '\n'
    attendeesList += attendee + ' would gain 0 happiness units by sitting next to Me\n'

  return attendeesList


def main():
  data = read_input("2015_13.txt")

  start_time = timer()
  print('Part 1: ' + str(knightsOfTheDinnerTable(data)))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))
  print()

  start_time = timer()
  print('Part 2: ' + str(knightsOfTheDinnerTable(addMe(data))))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))


if __name__ == '__main__':
  main()
