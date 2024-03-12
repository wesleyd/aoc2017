#!/usr/bin/env python3

import re

example_input = """
Generator A starts with 65
Generator B starts with 8921
"""

def extract_numbers(inp):
    return [int(x) for x in re.findall(r'\d+', inp)]

def gen(d, f, m=1):
    while True:
        d = (d * f) % 2147483647
        if d % m == 0:
            yield d

def count_matches(inp):
    a, b = extract_numbers(inp)
    gena = gen(a, 16807, 4)
    genb = gen(b, 48271, 8)
    n = 0
    for i in range(5_000_000):
        if next(gena) & 0xffff == next(genb) & 0xffff:
            n += 1
    return n

assert (got := count_matches(example_input)) == 309, got

with open('inputs/day15.input.txt') as f:
    real_input = f.read()
print(count_matches(real_input)) # => 313
