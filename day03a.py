#!/usr/bin/env python3

from math import ceil, sqrt

def spiral(n):
    assert n >= 0, n
    side, x, y = 1, 0, 0
    side = int(ceil(sqrt(n)))
    if side % 2 == 0:
        side += 1
    r = (side - 1) // 2
    x += r
    y -= r
    n -= side * side
    assert n <= 0, (n, side)
    if n == 0:
        return x,y
    # N is negative; count backwards from bottom right corner
    # Move left
    step = min(2*r, -n)
    x -= step
    n += step
    if n == 0:
        return x,y
    # Move up
    step = min(2*r, -n)
    y += step
    n += step
    if n == 0:
        return x,y
    # Move right
    step = min(2*r, -n)
    x += step
    n += step
    if n == 0:
        return x,y
    # Move down
    assert -n < 2*r, (n, r)
    y -= -n
    return x,y
assert (got := spiral(1)) == (0, 0), got
assert (got := spiral(2)) == (1, 0), got
assert (got := spiral(11)) == (2, 0), got
assert (got := spiral(49)) == (3, -3), got
assert (got := spiral(73)) == (-4, -4), got

def manhattan(p):
    return sum(abs(x) for x in p)

def run(n):
    return manhattan(spiral(n))

assert (got := run(1)) == 0, got
assert (got := run(12)) == 3, got
assert (got := run(23)) == 2, got
assert (got := run(1024)) == 31, got

with open('inputs/day03.input.txt') as f:
    real_input = int(f.read())
print(run(real_input)) # => 326

