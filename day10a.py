#!/usr/bin/env python3

import re

from itertools import chain

example_input = """
3, 4, 1, 5
"""

def extract_numbers(s):
    return [int(x) for x in re.findall(r'\d+', s)]

def run(inp, n=256):
    numbers = extract_numbers(inp)
    lst = list(range(n))
    pos = 0
    skip = 0
    def rev(length):
        for k in range(length//2):
            a, b = pos+k, pos+(length-k-1)
            lst[a%n], lst[b%n] = lst[b%n], lst[a%n]
    def pri():
        for i, x in enumerate(lst):
            if i == pos%n:
                print(f'[{x}] ', end='')
            else:
                print(f'{x} ', end='')
        print()
    for number in numbers:
        rev(number)
        pos += number
        pos += skip
        skip += 1
    return lst[0]*lst[1]
assert (got := run(example_input, 5)) == 12, got

with open('inputs/day10.input.txt') as f:
    real_input = f.read()
print(run(real_input))  # => 6952

