#!/usr/bin/env python3

import re

example_input = """
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
"""

class Tree:
    def __init__(self, inp):
        self.weight = {}
        self.children = {}
        self.parent = {}
        for line in inp.strip().splitlines():
            pieces = re.findall(r'[a-z0-9]+', line)
            name = pieces[0]
            self.weight[name] = int(pieces[1])
            children = pieces[2:]
            if children:
                self.children[name] = pieces[2:]
        for parent, children in self.children.items():
            for child in children:
                assert child not in self.parent, (child, self)
                self.parent[child] = parent
        all_nodes = set(self.weight)
        all_child_nodes = set(self.parent)
        root_nodes = all_nodes - all_child_nodes
        assert len(root_nodes) == 1, root_nodes
        self.root = next(iter(root_nodes))
    def __str__(self):
        return (f'Tree({self.root=}, {self.weight=}, '
                f'{self.children=}, {self.parent=}')
 
example_tree = Tree(example_input)
assert (got := example_tree.root) == 'tknk', got

with open('inputs/day07.input.txt') as f:
    real_input = f.read()
real_tree = Tree(real_input)

print(real_tree.root) # => bpvhwhh
