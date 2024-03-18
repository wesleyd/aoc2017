#!/usr/bin/env python3

from collections import defaultdict

class CPU:
    def __init__(self, inp):
        self.lines = inp.strip().splitlines()
        self.ram = [line.split() for line in self.lines]
        self.registers = defaultdict(int, {'a': 1})
        self.pc = 0
    def lookup(self, r):
        try:
            return int(r)
        except ValueError:
            return self.registers.get(r, 0)
    def state(self):
        line = self.lines[self.pc]
        s = f'pc={self.pc:2} : {line:13} '
        s += ' '.join(f'{k}={self.registers[k]}' for k in sorted(self.registers))
        if line.startswith('jnz'):
            s += '\n'
        return s
    def run(self):
        while True:
            print(self.state())
            match (instr := self.ram[self.pc]):
                case ('set', X, Y):
                    self.registers[X] = self.lookup(Y)
                case ('sub', X, Y):
                    self.registers[X] -= self.lookup(Y)
                case ('mul', X, Y):
                    self.registers[X] *= self.lookup(Y)
                case ('jnz', X, Y):
                    if self.lookup(X):
                        self.pc += self.lookup(Y) - 1
                case ('rem', *_):
                    continue
            self.pc += 1
            if self.pc < 0 or len(self.ram) <= self.pc:
                return self.lookup('h')

with open('inputs/day23.input.txt') as f:
    real_input = f.read()
#print(CPU(real_input).run()) # => 9409

def is_prime(b):
    i = 2
    while i < b//i + 1:
        if b % i == 0:
            return False
        i += 1
    return True

# STUDY THE CODE, it counts certain non-primes...
B = 99
B = 100_000 + 100 * B
C = B + 17_000
h = 0
for b in range(B, C+1, 17):
    if not is_prime(b):
        h += 1
# The answer is NOT 88
# 1452 is too high
print(h)
