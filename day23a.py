#!/usr/bin/env python3

from collections import defaultdict

class CPU:
    def __init__(self, inp):
        self.ram = [line.split() for line in inp.strip().splitlines()]
        self.registers = defaultdict(int)
        self.pc = 0
        self.nmul = 0
    def lookup(self, r):
        try:
            return int(r)
        except ValueError:
            return self.registers[r]
    def run(self):
        while True:
            match (instr := self.ram[self.pc]):
                case ('set', X, Y):
                    self.registers[X] = self.lookup(Y)
                case ('sub', X, Y):
                    self.registers[X] -= self.lookup(Y)
                case ('mul', X, Y):
                    self.registers[X] *= self.lookup(Y)
                    self.nmul += 1
                case ('jnz', X, Y):
                    if self.lookup(X):
                        self.pc += self.lookup(Y) - 1
            self.pc += 1
            if self.pc < 0 or len(self.ram) <= self.pc:
                return self.nmul

with open('inputs/day23.input.txt') as f:
    real_input = f.read()
print(CPU(real_input).run()) # => 9409
