#!/usr/bin/env python3

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

def move1(m, p):
    dx, dy = 0, 0
    if 'w' in m:
        dx = -1
    elif 'e' in m:
        dx = +1
    if m == 'n' or m in ('ne', 'nw') and p.x%2==0:
        dy = +1
    elif m == 's' or m in ('se', 'sw') and p.x%2==1:
        dy = -1
    return Point(p.x+dx, p.y+dy)

def dist(p, q=Point(0,0)):
    dx = abs(p.x - q.x)
    dy = abs(p.y - q.y)
    if p.y < 0:
        dy += 1
    return dx + dy - min(dy, dx)

def move(inp, p=Point(0,0)):
    furthest = 0
    q = p
    for m in inp.strip().split(','):
        q = move1(m, q)
        furthest = max(furthest, dist(p, q))
    return furthest

with open('inputs/day11.input.txt') as f:
    real_input = f.read()

print(move(real_input)) # => 1596
