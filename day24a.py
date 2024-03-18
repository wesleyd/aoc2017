#!/usr/bin/env python3

import math
import re

example_input = """
0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10
"""

def numbers(s):
    return [int(x) for x in re.findall(r'\d+', s)]

def parse(inp):
    return set([tuple(sorted(numbers(line))) for line in inp.strip().splitlines()])

with open('inputs/day24.input.txt') as f:
    real_input = f.read()

def bridges(bag, used=None):
    if not used:
        used = []
        want = 0
    else:
        want = used[-1][-1]
    for d in bag:
        if want in d:
            bag2 = bag - set([d])
            if d[0] != want:
                d = tuple(reversed(d))
            assert d[0] == want, (d, want)
            yield from bridge(bag2, used+[d])
    if used:
        yield used

def strength(bridge):
    n = 0
    if isinstance(bridge, int):
        return bridge
    for x in bridge:
        n += strength(x)
    return n

def strongest(bag):
    m = -math.inf
    for bridge in bridges(bag):
        if (st := strength(bridge)) > m:
            m = st
    return m
assert (got := strongest(parse(example_input))) == 31, got

print(strongest(parse(real_input))) # => 1868
