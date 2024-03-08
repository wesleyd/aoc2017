#!/usr/bin/env python3

def captcha(s):
    n = 0
    def antipode(i):
        return (i + len(s)//2) % len(s)
    for i in range(len(s)):
        if (c := s[i]) == s[antipode(i)]:
            n += int(c)
    return n
assert (c := captcha('1212')) == 6, c
assert (c := captcha('1221')) == 0, c
assert (c := captcha('123425')) == 4, c
assert (c := captcha('123123')) == 12, c
assert (c := captcha('12131415')) == 4, c

with open('inputs/day01.input.txt') as f:
    real_input = f.read().strip()

print(captcha(real_input)) # => 1076
