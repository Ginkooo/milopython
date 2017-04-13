#!/usr/bin/python

import sys
from itertools import permutations
from datetime import date

def combine_date(year, month, day):
    if year < 2000: year += 2000
    try:
        return date(year, month, day)
    except:
        return None

filename=sys.argv[1]

with open(filename) as f:
    line = f.readline().strip()
    part1, part2, part3 = map(int, line.split('/'))
parts = sorted([part1, part2, part3])

dates = []

for thing in permutations(parts, len(parts)):
    res = combine_date(*thing)
    if res is not None: dates.append(res)

if not dates:
    print('{} is illegal'.format(line))
else:
    print('{:%Y-%m-%d}'.format(min(dates)))
