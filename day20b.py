#!/usr/bin/env python3

import math
import re

from collections import defaultdict, namedtuple

example_input = """
p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>
p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>
p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>
p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>
"""

Particle = namedtuple('Particle', ['X', 'Y', 'Z'])
PVA = namedtuple('PVA', ['P', 'V', 'A'])

def numbers(s):
    return [int(x) for x in re.findall(r'[+-]?\d+', s)]

def make_particle(px, py, pz, vx, vy, vz, ax, ay, az):
    return Particle(X=PVA(px, vx, ax), Y=PVA(py,vy,ay), Z=PVA(pz,vz,az))

def parse(inp):
    return [make_particle(*numbers(line)) for line in inp.strip().splitlines()]

def collide_pva(pva1, pva2):
    """Return the integer, t >= 0 times at which pva1 and pva2 collide."""
    tt = set()
    if pva1.A == pva2.A:
        # It's not quadratic, it's linear...
        if pva2.V == pva1.V:
            # Nope, it's not even linear...
            if pva1.P == pva2.P:
                return 'always'  # *Always* collides
            else:
                return set() # Never collids
        else:
            tt.add(round((pva1.P - pva2.P) / (pva2.V - pva1.V)))
    else:
        # OK, it's quadratic...
        a = (pva1.A - pva2.A) / 2
        b = pva1.V - pva2.V + a
        c = pva1.P - pva2.P
        s2 = b*b - 4*a*c
        if s2 < 0:
            return set()  # Never collides
        s = math.sqrt(s2)
        tt.add((-b+s)/(2*a))
        tt.add((-b-s)/(2*a))
    ret = set()
    for t in tt:
        # Only future collisions
        if t < 0:
            continue
        # Make sure t is *really* an integer, by re-substituting
        t = round(t)
        tt1_2 = t*(t+1)/2
        z1 = pva1.P + t*pva1.V + tt1_2*pva1.A
        z2 = pva2.P + t*pva2.V + tt1_2*pva2.A
        if z1 == z2:
            ret.add(t)
    return ret

def collide(p1, p2):
    tt = None
    for s in [collide_pva(p1.X, p2.X), collide_pva(p1.Y, p2.Y), collide_pva(p1.Z, p2.Z)]:
        if s == 'always':
            continue
        if tt is None:
            tt = s
        else:
            tt &= s
    assert len(tt) <= 1, (p1, p2, tt)
    for t in tt:
        return t

def run(particles):
    bang = defaultdict(set)
    alive = set(particles)
    for i in range(len(particles)):
        for j in range(i+1, len(particles)):
            if (t := collide(particles[i], particles[j])):
                bang[t].add(particles[i])
                bang[t].add(particles[j])
    for t, colliders in bang.items():
        colliders &= alive
        if len(colliders) <= 1:
            continue
        for p in colliders:
            alive.discard(p)
    return len(alive)

assert (got := run(parse(example_input))) == 1, got

with open('inputs/day20.input.txt') as f:
    real_input = f.read()
print(run(parse(real_input))) # => 448
