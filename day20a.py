#!/usr/bin/env python3

import math
import re

from collections import namedtuple

example_input = """
p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>
"""

Particle = namedtuple('Particle', ['Pos', 'Vel', 'Acc'])
XYZ = namedtuple('XYZ', ['X', 'Y', 'Z'])

def numbers(s):
    return [int(x) for x in re.findall(r'\d+', s)]

def parse_particle(line):
    pva = line.split(">,")
    return Particle(*[XYZ(*numbers(chunk)) for chunk in pva])

def parse(inp):
    return [parse_particle(line) for line in inp.strip().splitlines()]
    
def manhattan(xyz):
    return abs(xyz.X) + abs(xyz.Y) + abs(xyz.Z)

def min_many(lst, key):
    m = math.inf
    res = []
    for x in lst:
        if (k := key(x)) < m:
            m = k
            res = [x]
        elif k == m:
            res.append(x)
    return res
    
def eventually_nearest(particles):
    indices = range(len(particles))
    indices = min_many(indices, key=lambda i: manhattan(particles[i].Acc))
    indices = min_many(indices, key=lambda i: manhattan(particles[i].Vel))
    indices = min_many(indices, key=lambda i: manhattan(particles[i].Pos))
    # This mightn't work if there are minus signs in there, but there aren't.
    assert len(indices) == 1, indices
    return indices[0]
assert (got := eventually_nearest(parse(example_input))) == 0, got

with open('inputs/day20.input.txt') as f:
    real_input = f.read()
print(eventually_nearest(parse(real_input))) # => 457
