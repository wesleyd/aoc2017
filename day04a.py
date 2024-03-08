#!/usr/bin/env python3

def valid(line):
    words = line.split()
    return len(set(words)) == len(words)
assert (got := valid("aa bb cc dd ee")), got
assert not (got := valid("aa bb cc dd aa")), got
assert (got := valid("aa bb cc dd aaa")), got

def run(inp):
    valids = [valid(line) for line in inp.strip().splitlines()]
    return valids.count(True)

with open('inputs/day04.input.txt') as f:
    real_input = f.read()
print(run(real_input))  # => 386
