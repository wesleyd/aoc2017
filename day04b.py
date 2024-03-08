#!/usr/bin/env python3

def valid(line):
    words = []
    for word in line.split():
        letters = list(word)
        letters.sort()
        word = ''.join(letters)
        words.append(word)
    return len(set(words)) == len(words)
assert (got := valid("abcde fghij")), got
assert not (got := valid("abcde xyz ecdab")), got
assert (got := valid("a ab abc abd abf abj")), got
assert (got := valid("iiii oiii ooii oooi oooo")), got
assert not (got := valid("oiii ioii iioi iiio")), got

def run(inp):
    valids = [valid(line) for line in inp.strip().splitlines()]
    return valids.count(True)

with open('inputs/day04.input.txt') as f:
    real_input = f.read()
print(run(real_input))  # => 208
