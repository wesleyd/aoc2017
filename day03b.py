#!/usr/bin/env python3

def spiral():
    """Yields (x,y) around the spiral forever."""
    d = {}
    x, y = 0, 0
    yield x,y
    r = 1
    while True:
        x += 1
        y -= 1
        for q in range(2*r):
            y += 1
            yield x,y
        for q in range(2*r):
            x -= 1
            yield x,y
        for q in range(2*r):
            y -= 1
            yield x,y
        for q in range(2*r):
            x += 1
            yield x,y
        r += 1

def neighbor_sum():
    """Yields the neighbor sums around the spiral."""
    gen = spiral()
    d = {next(gen): 1}
    yield 1
    def neighbors(p):
        X, Y = p
        for x in range(X-1, X+2):
            for y in range(Y-1, Y+2):
                if x == X and y == Y:
                    continue
                yield d.get((x,y), 0)
    for p in gen:
        d[p] = sum(neighbors(p))
        yield d[p]

def run(inp):
    n = int(inp)
    for x in neighbor_sum():
        if x > n:
            return x
        
with open('inputs/day03.input.txt') as f:
    real_input

print(run(real_input)) # => 363010
