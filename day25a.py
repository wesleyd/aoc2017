#!/usr/bin/env python3

import re

from collections import namedtuple
from dataclasses import dataclass

example_input = """
Begin in state A.
Perform a diagnostic checksum after 6 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state B.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.
"""

Action = namedtuple('Action', ['write', 'move', 'then'])

class Turing:
    def __init__(self, inp):
        self.pos = 0
        self.tape = {}
        self.rules = {}
        paras = inp.strip().split('\n\n')
        m = re.search(r'state ([A-Z])\.', paras[0])
        self.state = m.group(1)
        m = re.search(r'after (\d+) steps', paras[0])
        self.steps = int(m.group(1))
        for para in paras[1:]:
            m_in = re.findall(r'In state ([A-Z]):', para)
            start = m_in[0]
            m_curr = re.findall('current value is ([01]):', para)
            m_write = re.findall('Write the value ([01])\.', para)
            m_move = re.findall('Move one slot to the (left|right)\.', para)
            m_then = re.findall('Continue with state ([A-Z])\.', para)
            #print(m_in, m_curr, m_write, m_move, m_then)
            for g in (0,1):
                a = (start, int(m_curr[g]))
                z = Action(write=int(m_write[g]), move=m_move[g], then=m_then[g])
                self.rules[a] = z
        #print(self)
    def __str__(self):
        return f'({self.state}, {self.pos}) rules={self.rules} tape={self.tape}'
    def run(self, steps=None):
        if steps is None:
            steps = self.steps
        for i in range(steps):
            at = (self.state, self.tape.get(self.pos, 0))
            action = self.rules[at]
            assert action.move in ('left', 'right')
            self.tape[self.pos] = int(action.write)
            if action.move == 'left':
                self.pos -= 1
            else:
                self.pos += 1
            self.state = action.then
        return sum(self.tape.values())
            
assert (got := Turing(example_input).run()) == 3, got

with open('inputs/day25.input.txt') as f:
    real_input = f.read()

print(Turing(real_input).run())

