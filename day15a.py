#!/usr/bin/env python3

import re

example_input = """
Generator A starts with 65
Generator B starts with 8921
"""

def extract_numbers(inp):
    return [int(x) for x in re.findall(r'\d+', inp)]

def count_matches(inp):
    a, b = extract_numbers(inp)
    n = 0
    for i in range(40_000_000):
        a = (a * 16807) % 2147483647
        b = (b * 48271) % 2147483647
        if a & 0xffff == b & 0xffff:
            n += 1
    return n


assert (got := count_matches(example_input)) == 588, got

with open('inputs/day15.input.txt') as f:
    real_input = f.read()
print(count_matches(real_input)) # => 600
