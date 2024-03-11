#!/usr/bin/env python3

import re

from collections import namedtuple

example_input = """
0: 3
1: 2
4: 4
6: 4
"""

Scanner = namedtuple('Scanner', ['layer', 'depth'])

def numbers(line):
    return [int(x) for x in re.findall(r'\d+', line)]

def parse(inp):
    return [Scanner(*numbers(line)) for line in inp.strip().splitlines()]

def caught(scanners, n):
    severity = 0
    for scanner in scanners:
        mod = 2*(scanner.depth-1)
        t = n + scanner.layer
        if t % mod == 0:
            return True
    return False

def run(inp):
    scanners = parse(inp)
    i = 0
    while True:
        if not caught(scanners, i):
            return i
        i += 1

assert (got := run(example_input)) == 10, got

with open('inputs/day13.input.txt') as f:
    real_input = f.read()

print(run(real_input))  # => 3878062
