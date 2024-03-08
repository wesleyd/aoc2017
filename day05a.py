#!/usr/bin/env python3

import re

example_input = """
0
3
0
1
-3
"""

def numbers(s):
    return [int(x) for x in re.findall(r'[+-]?\d+', s)]

def run(inp):
    ram = numbers(inp)
    pc = 0
    steps = 0
    while 0 <= pc < len(ram):
        n = ram[pc]
        ram[pc] += 1
        pc += n
        steps += 1
    return steps
assert (got := run(example_input)) == 5, got

with open('inputs/day05.input.txt') as f:
    real_input = f.read()
print(run(real_input)) # => 391540
