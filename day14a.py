#!/usr/bin/env python3

def knot_hash(s, n=256):
    numbers = [ord(c) for c in s] + [17, 31, 73, 47, 23]
    lst = list(range(n))
    pos = 0
    skip = 0
    def rev(length):
        for k in range(length//2):
            a, b = pos+k, pos+(length-k-1)
            lst[a%n], lst[b%n] = lst[b%n], lst[a%n]
    def pri():
        for i, x in enumerate(lst):
            if i == pos%n:
                print(f'[{x}] ', end='')
            else:
                print(f'{x} ', end='')
        print()
    for _ in range(64):
        for number in numbers:
            rev(number)
            pos += number
            pos += skip
            skip += 1
    s = ''
    for j in range(n//16):
        h = 0
        for k in range(16):
            h ^= lst[j*16+k]
        s += f'{h:08b}'
    return s.replace('0', '.').replace('1', '#')

def defrag_count(inp):
    n = 0
    inp = inp.strip()
    for i in range(128):
        s = f'{inp}-{i}'
        kh = knot_hash(s)
        n += kh.count('#')
    return n

assert (got := defrag_count('flqrgnkx')) == 8108, got

with open('inputs/day14.input.txt') as f:
    real_input = f.read()
print(defrag_count(real_input)) # => 8194
