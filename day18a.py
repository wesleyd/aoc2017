#!/usr/bin/env python3

import re

from collections import defaultdict

example_input = """
set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2
"""

class CPU(object):
    def __init__(self, inp):
        self.registers = defaultdict(int)
        self.pc = 0
        self.last_sound = None
        self.ram = inp.strip().splitlines()
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
                    self.last_sound = self.lookup(X)
                case ('set', X, Y):
                    self.registers[X] = self.lookup(Y)
                case ('add', X, Y):
                    self.registers[X] += self.lookup(Y)
                case ('mul', X, Y):
                    self.registers[X] *= self.lookup(Y)
                case ('mod', X, Y):
                    self.registers[X] %= self.lookup(Y)
                case ('rcv', X):
                    if self.lookup(X):
                        return self.last_sound
                case ('jgz', X, Y):
                    if self.lookup(X) > 0:
                        self.pc += self.lookup(Y)
                        self.pc -= 1
            self.pc += 1

assert (got := CPU(example_input).play()) == 4, got

with open('inputs/day18.input.txt') as f:
    real_input = f.read()
print(CPU(real_input).play()) # => 4601
