#!/usr/bin/env python3

import re

from collections import defaultdict, deque

example_input = """
snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d
"""

class Thread(object):
    def __init__(self, inp, p):
        self.ram = inp.strip().splitlines()
        self.registers = defaultdict(int)
        self.registers['p'] = p
        self.queue = deque()
        self.other = None
        self.nsends = 0
        self.pc = 0
    def lookup(self, r):
        try:
            return int(r)
        except ValueError:
            return self.registers[r]
    def play(self):
        while True:
            instr = self.ram[self.pc]
            pieces = instr.split()
            match pieces:
                case ('snd', X):
                    self.nsends += 1
                    self.other.queue.append(self.lookup(X))
                case ('set', X, Y):
                    self.registers[X] = self.lookup(Y)
                case ('add', X, Y):
                    self.registers[X] += self.lookup(Y)
                case ('mul', X, Y):
                    self.registers[X] *= self.lookup(Y)
                case ('mod', X, Y):
                    self.registers[X] %= self.lookup(Y)
                case ('rcv', X):
                    if not self.queue:
                        return
                    self.registers[X] = self.queue.popleft()
                case ('jgz', X, Y):
                    if self.lookup(X) > 0:
                        self.pc += self.lookup(Y)
                        self.pc -= 1
            self.pc += 1

def run(inp):
    t0 = Thread(inp, 0)
    t1 = Thread(inp, 1)
    t0.other, t1.other = t1, t0
    while True:
        t0.play()
        t1.play()
        if not t0.queue and not t1.queue:
            break
    return t1.nsends
assert (got := run(example_input)) == 3, got

with open('inputs/day18.input.txt') as f:
    real_input = f.read()
print(run(real_input))   # => 6858
