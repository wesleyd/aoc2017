#!/usr/bin/env python3

import re

example_input = """
5 1 9 5
7 5 3
2 4 6 8
"""

def numbers(s):
    for t in re.findall(r'\d+', s):
        yield int(t)

def checksum(inp):
    cs = 0
    for line in inp.strip().splitlines():
        nn = list(numbers(line))
        cs += max(nn) - min(nn)
    return cs
assert (got := checksum(example_input)) == 18, got

with open('inputs/day02.input.txt') as f:
    real_input = f.read()

print(checksum(real_input)) # => 54426
