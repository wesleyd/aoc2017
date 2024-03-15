#!/usr/bin/env python3

example_input = """
     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ 
"""

BACK = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
LEFT = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
RIGHT = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}

class Maze(object):
    def __init__(self, inp):
        self.g = inp.splitlines()
    def start(self):
        for i in range(len(self.g)):  # Blank first line?
            if '|' in self.g[i]:
                return (i, self.g[i].index('|'))
    def at(self, p):
        row, col = p
        if row < 0 or len(self.g) <= row or col < 0 or len(self.g[row]) <= col:
            return ' '
        return self.g[row][col]
    def move(self, p, v):
        row, col = p
        for w in [v, LEFT[v], RIGHT[v]]:
            match w:
                case 'N':
                    q = (row-1, col)
                case 'S':
                    q = (row+1, col)
                case 'E':
                    q = (row, col+1)
                case 'W':
                    q = (row, col-1)
            c = self.at(q)
            if c != ' ':
                return (q, w, c)
        return None, None, None
        
def run(inp):
    maze = Maze(inp)
    p, v = maze.start(), 'S'
    c = maze.at(p)
    n = 0
    while p:
        p, v, c = maze.move(p, v)
        n += 1
    return n

assert (got := run(example_input)) == 38, got

with open('inputs/day19.input.txt') as f:
    real_input = f.read()
print(run(real_input)) # => 18702
