#!/usr/bin/env python3

example_input = """
3
""".strip()

def print_buf(buf, i):
    for j, x in enumerate(buf):
        if i == j:
            print(f'({buf[j]}) ', end='')
        else:
            print(f' {buf[j]}  ', end='')
    print()

def run(inp):
    step = int(inp)
    p = 0
    buf = [0]
    for i in range(1,2017+1):
        p = (p + step) % len(buf)
        buf.insert(p+1, i)
        p = (p + 1) % len(buf)
    return buf[(p+1)%len(buf)]

assert (got := run(example_input)) == 638, got

with open('inputs/day17.input.txt') as f:
    real_input = f.read().strip()


print(run(real_input)) # => 1025
