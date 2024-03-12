#!/usr/bin/env python3

example_input = """
s1,x3/4,pe/b
"""

def parse(inp):
    steps = []
    for line in inp.strip().split(','):
        if (m := re.match(r's(\d+)', line)):
            steps.append(('Spin', int(m.group(1))))
        elif (m := re.match(r'x([0-9]+)/([0-9]+)', line)):
            steps.append(('Exchange', int(m.group(1)), int(m.group(2))))
        elif (m := re.match(r'p([a-z])/([a-z])', line)):
            steps.append(('Partner', m.group(1), m.group(2)))
        else:
            assert False, line
    return steps

def dance(steps, dancers=16):
    lineup = [chr(ord('a') + i) for i in range(dancers)]
    for step in steps:
        match step:
            case ('Spin', n):
                lineup = lineup[-n:] + lineup[:-n]
            case ('Exchange', m, n):
                lineup[m], lineup[n] = lineup[n], lineup[m]
            case ('Partner', x, y):
                lineup = [y  if c == x else x if c == y else c for c in lineup]
    return ''.join(lineup)

example_steps = parse(example_input)
assert (got := dance(example_steps, 5)) == 'baedc', got

with open('inputs/day16.input.txt') as f:
    real_input = f.read()
print(dance(parse(real_input))) => 'olgejankfhbmpidc'

