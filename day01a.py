#!/usr/bin/env python3

def captcha(s):
    n = 0
    def at(k):
        return s[k%len(s)]
    for i in range(len(s)):
        if (c := at(i)) == at(i+1):
            n += int(c)
    return n
assert captcha('1122') == 3
assert captcha('1111') == 4
assert captcha('1234') == 0
assert captcha('91212129') == 9

with open('inputs/day01.input.txt') as f:
    real_input = f.read().strip()

print(captcha(real_input))
