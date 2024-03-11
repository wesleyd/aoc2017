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

def move(inp, p=Point(0,0)):
    for m in inp.strip().split(','):
        p = move1(m, p)
    return p

assert (got := move('n'))  == Point( 0,+1), got
assert (got := move('ne')) == Point(+1,+1), got
assert (got := move('se')) == Point(+1, 0), got
assert (got := move('s'))  == Point( 0,-1), got
assert (got := move('sw')) == Point(-1, 0), got
assert (got := move('nw')) == Point(-1,+1), got

assert (got := move('n',  Point(1,1))) == Point( 1,+2), got
assert (got := move('ne', Point(1,1))) == Point(+2,+1), got
assert (got := move('se', Point(1,1))) == Point(+2, 0), got
assert (got := move('s',  Point(1,1))) == Point( 1, 0), got
assert (got := move('sw', Point(1,1))) == Point( 0, 0), got
assert (got := move('nw', Point(1,1))) == Point( 0,+1), got

def dist(p, q=Point(0,0)):
    dx = abs(p.x - q.x)
    dy = abs(p.y - q.y)
    if p.y < 0:
        dy += 1
    return dx + dy - min(dy, dx)

assert (got := dist(move('ne,ne,ne'))) == 3, got
assert (got := dist(move('ne,ne,sw,sw'))) == 0, got
assert (got := dist(move('ne,ne,s,s'))) == 2, got
assert (got := dist(move('se,se'))) == 2, got
assert (got := dist(move('se,sw,se,sw,sw'))) == 3, got

with open('inputs/day11.input.txt') as f:
    real_input = f.read()

print(dist(move(real_input))) # => 818
