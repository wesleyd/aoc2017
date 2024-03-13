#!/usr/bin/env python3

def after_zero_after(step, n=50_000_000):
    """Returns the number after zero after n iterations."""
    after_zero = 1
    bufsize = 2
    spinlock = 1
    for i in range(2, n+1):
        spinlock = (spinlock + step) % bufsize
        if spinlock == 0:
            after_zero = i
        bufsize += 1
        spinlock = (spinlock + 1) % bufsize
    return after_zero

with open('inputs/day17.input.txt') as f:
    real_input = f.read().strip()

print(after_zero_after(int(real_input)))  # => 37803463
