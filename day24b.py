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

def all_bridges(bag, used=None):
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

def strongest(bridges):
    m = -math.inf
    for bridge in bridges:
        if (st := strength(bridge)) > m:
            m = st
    return m
assert (got := strongest(all_bridges(parse(example_input)))) == 31, got

def longests(bridges):
    m = -math.inf
    ret = []
    for bridge in bridges:
        l = len(bridge)
        if l > m:
            m = l
            ret = [bridge]
        elif l == m:
            ret.append(bridge)
    return ret

print(strongest(longests(all_bridges(parse(real_input))))) # => 1841
