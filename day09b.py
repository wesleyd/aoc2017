#!/usr/bin/env python3

def parse(inp):
    garbage = 0
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
            elif c == '!':
                cancel_next = True
            else:
                garbage += 1
        #elif c == '{':
        #    depth += 1
        #    sc += depth
        #elif c == '}':
        #    depth -= 1
        elif c == '<':
            in_garbage = True
    return garbage

assert (got := parse('<>')) ==  0, got
assert (got := parse('<random characters>')) ==  17, got
assert (got := parse('<<<<>')) ==  3, got
assert (got := parse('<{!>}>')) ==  2, got
assert (got := parse('<!!>')) ==  0, got
assert (got := parse('<!!!>>')) ==  0, got
assert (got := parse('<{o"i!a,<{i<a>')) ==  10, got

with open('inputs/day09.input.txt') as f:
    real_input = f.read()
print(parse(real_input)) # => 7825 
