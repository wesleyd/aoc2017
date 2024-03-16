#!/usr/bin/env python3

example_input = """
../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#
"""

START = tuple("""
.#.
..#
###
""".strip().splitlines())

def rot(p):
    ss = []
    for i in (range(len(p)-1,-1,-1)):
        ss.append(''.join([p[j][i] for j in range(len(p))]))
    return tuple(ss)

def flip(p):
    ss = []
    for i in (range(len(p)-1,-1,-1)):
        ss.append(''.join([p[i][j] for j in range(len(p))]))
    return tuple(ss)

def parse(inp):
    rules = {}
    for line in inp.strip().splitlines():
        l, r = line.split(' => ')
        l, r = tuple(l.split('/')), tuple(r.split('/'))
        k = flip(l)
        for _ in range(4):
            rules[l] = r
            rules[k] = r
            l = rot(l)
            k = rot(k)
    return rules
example_rules = parse(example_input)

def split(s):
    ret = []
    N = len(s)
    if N % 2 == 0:
        M = 2
    else:
        M = 3
    for r in range(N//M):
        row = []
        for c in range(N//M):
            lines = []
            for ln in range(M):
                lines.append(s[M*r+ln][M*c:M*c+M])
            row.append(tuple(lines))
        ret.append(row)
    return ret

def join(t):
    lines = []
    M = len(t[0][0])
    for row in t:
        for l in range(M):
            line = ''
            for sq in row:
                line += sq[l]
            lines.append(line)
    return tuple(lines)

def applyN(rules, n=1, s=START):
    while n:
        t = split(s)
        for i, row in enumerate(t):
            for j, chunk in enumerate(row):
                for l,r in rules.items():
                    if l == chunk:
                        t[i][j] = r
                        break
        s = join(t)
        n -= 1
    return s

def lit(s):
    n = 0
    for g in s:
        for c in g:
            if c == '#':
                n += 1
    return n
assert (got := lit(applyN(example_rules, 2))) == 12, got

with open('inputs/day21.input.txt') as f:
    real_input = f.read()
real_rules = parse(real_input)
print(lit(applyN(real_rules, 18))) # => 2536879

