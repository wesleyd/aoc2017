#!/usr/bin/env python3

from collections import defaultdict, deque

example_input = """
0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
"""

def parse(inp):
    pipes = defaultdict(set)
    for line in inp.strip().splitlines():
        l, rr = line.split(' <-> ')
        l = int(l)
        for r in rr.split(','):
            pipes[l].add(int(r))
    return pipes

def walk(pipes, p=0):
    seen = set()
    future = deque([p])
    while future:
        p = future.popleft()
        if p in seen:
            continue
        seen.add(p)
        for q in pipes[p]:
            if q not in seen:
                future.append(q)
    return seen

def run(inp):
    return len(walk(parse(inp)))
 
assert (got := run(example_input)) == 6, got

with open('inputs/day12.input.txt') as f:
    real_input = f.read()
print(run(real_input)) # => 288
