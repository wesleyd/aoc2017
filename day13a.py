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

def caught(scanners):
    severity = 0
    for scanner in scanners:
        mod = 2*(scanner.depth-1)
        if scanner.layer % mod == 0:
            severity += scanner.layer * scanner.depth
    return severity

def run(inp):
    return caught(parse(inp))

assert (got := run(example_input)) == 24, got

with open('inputs/day13.input.txt') as f:
    real_input = f.read()

print(run(real_input))  # => 3184
