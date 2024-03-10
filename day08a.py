#!/usr/bin/env python3

from collections import defaultdict

import re

example_input = """
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
"""

def transform(inp):
    commands = []
    for line in inp.strip().splitlines():
        if (m := re.match(r'([a-z]+) (inc|dec) ([+-]?\d+) if ([a-z]+) (\S+) ([+-]?\d+)', line)):
            r, cmd, n, q, op, x = m.groups()
            if cmd == 'inc':
                inc = '+='
            else:
                inc = '-='
            commands.append(f'if d["{q}"] {op} {x}:\n  d["{r}"] {inc} {n}')
        else:
            assert False, f'bad line {line=}'
    return '\n'.join(commands)

def run(inp):
    d = defaultdict(int)
    exec(transform(inp))
    return max(d.values())
assert (got := run(example_input)) == 1, got

with open('inputs/day08.input.txt') as f:
    real_input = f.read()
print(run(real_input)) # => 4647
