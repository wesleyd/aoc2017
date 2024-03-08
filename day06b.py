#!/usr/bin/env python3

import re

example_input = """
0 2 7 0
"""

def parse(inp):
    return tuple(int(x) for x in re.findall(r'\d+', inp))

def redistribute(banks):
    banks = list(banks)
    m = max(banks)
    n = banks.index(m)
    banks[n] = 0
    for i in range(len(banks)):
        banks[i] += m // len(banks)
    m %= len(banks)
    while m:
        n += 1
        if n >= len(banks):
            n = 0
        banks[n] += 1
        m -= 1
    return tuple(banks)

def run(inp):
    prev = {}
    banks = parse(inp)
    step = 1
    while True:
        banks = redistribute(banks)
        if banks in prev:
            return step - prev[banks]
        prev[banks] = step
        step += 1

assert (got := run(example_input)) == 4, got

with open('inputs/day06.input.txt') as f:
    real_input = f.read()

print(run(real_input)) # => 1086
