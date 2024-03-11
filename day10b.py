#!/usr/bin/env python3

import re

from itertools import chain

example_input = """
3, 4, 1, 5
"""

def run(inp, n=256):
    numbers = [ord(c) for c in inp.strip()] + [17, 31, 73, 47, 23]
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
    for _ in range(64):
        for number in numbers:
            rev(number)
            pos += number
            pos += skip
            skip += 1
    s = ''
    for j in range(16):
        h = 0
        for k in range(16):
            h ^= lst[j*16+k]
        s += f'{h:02x}'
    return s
assert (got := run('')) == 'a2582a3a0e66e6e86e3812dcb672a272', got


with open('inputs/day10.input.txt') as f:
    real_input = f.read()
print(run(real_input))  # => 28e7c4360520718a5dc811d3942cf1fd
