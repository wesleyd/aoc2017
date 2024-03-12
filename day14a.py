#!/usr/bin/env python3

from collections import deque

def knot_hash(s, n=256):
    numbers = [ord(c) for c in s] + [17, 31, 73, 47, 23]
    lst = list(range(n))
    pos = 0
    skip = 0
    def rev(length):
        for k in range(length//2):
            a, b = pos+k, pos+(length-k-1)
            lst[a%n], lst[b%n] = lst[b%n], lst[a%n]
    def pri():
        for i, x in enumerate(lst):
            if i == pos%n:
                print(f'[{x}] ', end='')
            else:
                print(f'{x} ', end='')
        print()
    for _ in range(64):
        for number in numbers:
            rev(number)
            pos += number
            pos += skip
            skip += 1
    s = ''
    for j in range(n//16):
        h = 0
        for k in range(16):
            h ^= lst[j*16+k]
        s += f'{h:08b}'
    return s.replace('0', '.').replace('1', '#')

def defrag(inp):
    ss = []
    inp = inp.strip()
    for i in range(128):
        s = f'{inp}-{i}'
        kh = knot_hash(s)
        ss.append(kh)
    return ss

def walk(ss, r, c):
    island = set()
    futures = deque()
    futures.append((r, c))
    while futures:
        r, c = futures.popleft()
        island.add((r, c))
        for r2, c2 in [ (r-1, c), (r+1, c), (r, c+1), (r, c-1) ]:
            if r2 < 0 or len(ss) <= r2 or c2 < 0 or len(ss[r2]) <= c2:
                continue
            if (r2, c2) in island:
                continue
            if ss[r2][c2] == '#':
                futures.append((r2, c2))
    return island

def count_islands(ss):
    all_islands = set()
    num_islands = 0
    for row, line in enumerate(ss):
        for col, ch in enumerate(line):
            if ch != '#':
                continue
            if (row, col) in all_islands:
                continue
            island = walk(ss, row, col)
            if island:
                num_islands += 1
                #print(island)
                all_islands.update(island)
    return num_islands

example_input = """
flqrgnkx
"""

assert (got := count_islands(defrag(example_input)) == 1242), got

with open('inputs/day14.input.txt') as f:
    real_input = f.read()
print(count_islands(defrag(real_input))) # => 1141
