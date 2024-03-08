#!/usr/bin/env python3

import re

example_input = """
5 9 2 8
9 4 7 3
3 8 6 5
"""

def numbers(s):
    for t in re.findall(r'\d+', s):
        yield int(t)

def sum_divizors(nn):
    for i, a in enumerate(nn):
        for b in nn[i+1:]:
            assert a > b  # We sorted them!
            if a % b == 0:
                return a // b

def checksum(inp):
    cs = 0
    for line in inp.strip().splitlines():
        nn = list(numbers(line))
        nn.sort(reverse=True)
        cs += sum_divizors(nn)
    return cs
assert (got := checksum(example_input)) == 9, got

with open('inputs/day02.input.txt') as f:
    real_input = f.read()

print(checksum(real_input)) # => 333
