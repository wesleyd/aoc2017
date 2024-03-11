#!/usr/bin/env python3

def parse(inp):
    ngroups = 0
    sc = 0
    depth = 0
    in_garbage = False
    cancel_next = False
    for c in inp.strip():
        if cancel_next:
            cancel_next = False
            continue
        elif in_garbage:
            if c == '>':
                in_garbage = False
            if c == '!': cancel_next = True
        elif c == '{':
            ngroups += 1
            depth += 1
            sc += depth
        elif c == '}':
            depth -= 1
        elif c == '<':
            in_garbage = True
    return sc

assert (got := parse('{}')) == 1, got
assert (got := parse('{{{}}}')) == 6, got
assert (got := parse('{{},{}}')) == 5, got
assert (got := parse('{{{},{},{{}}}}')) == 16, got
assert (got := parse('{<a>,<a>,<a>,<a>}')) == 1, got
assert (got := parse('{{<ab>},{<ab>},{<ab>},{<ab>}}')) == 9, got
assert (got := parse('{{<!!>},{<!!>},{<!!>},{<!!>}}')) == 9, got
assert (got := parse('{{<a!>},{<a!>},{<a!>},{<ab>}}')) == 3, got

with open('inputs/day09.input.txt') as f:
    real_input = f.read()
print(parse(real_input)) # => 17390
