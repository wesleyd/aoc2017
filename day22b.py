#!/usr/bin/env python3

from collections import defaultdict, namedtuple

example_input = """
..#
#..
...
"""

P = namedtuple('P', ['x', 'y'])

LEFT = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
RIGHT = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}

def move(p, v):
    assert v in 'NSEW', (p, v)
    match v:
        case 'N':
            return P(p.x, p.y+1)
        case 'S':
            return P(p.x, p.y-1)
        case 'E':
            return P(p.x+1, p.y)
        case 'W':
            return P(p.x-1, p.y)

class Grid:
    def __init__(self, inp):
        self.p = P(0,0)
        self.v = 'N'
        self.g = defaultdict(str)
        lines = inp.strip().splitlines()
        r = len(lines) // 2
        for row, line in enumerate(lines):
            for col, ch in enumerate(line):
                if ch == '#':
                    x, y = col - r, r - row
                    self.g[P(x,y)] = '#'
        self.infected = 0
    def walk1(self):
        match self.g.get(self.p, '.'):
            case '.':
                self.v = LEFT[self.v]
                self.g[self.p] = 'W'
            case 'W':
                self.g[self.p] = '#'
                self.infected += 1
            case '#':
                self.v = RIGHT[self.v]
                self.g[self.p] = 'F'
            case 'F':
                self.v = RIGHT[RIGHT[self.v]]  # Reverse
                self.g[self.p] = '.'
        self.p = move(self.p, self.v)

def run(inp, n):
    g = Grid(inp)
    for i in range(n):
        g.walk1()
    return g.infected

assert (got := run(example_input, 100)) == 26, got
assert (got := run(example_input, 10000000)) == 2511944, got

with open('inputs/day22.input.txt') as f:
    real_input = f.read()

print(run(real_input, 10000000)) # => 2512022
