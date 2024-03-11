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

def walk(pipes):
    all_seen = set()
    ngroups = 0
    for p in pipes:
        if p in all_seen:
            continue
        seen = set()
        future = deque([p])
        while future:
            q = future.popleft()
            if q in seen:
                continue
            seen.add(q)
            for r in pipes[q]:
                if r not in seen:
                    future.append(r)
        all_seen.update(seen)
        ngroups += 1
    return ngroups

def run(inp):
    return walk(parse(inp))
 
assert (got := run(example_input)) == 2, got

with open('inputs/day12.input.txt') as f:
    real_input = f.read()
print(run(real_input)) # => 211
