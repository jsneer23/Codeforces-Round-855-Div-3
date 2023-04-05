""" Solves Problem A """

import sys

sys.stdin = open('A/input.txt', 'r', encoding="utf8")
input = lambda: sys.stdin.readline().rstrip()

def main():
    """ Main Function """

    input()
    word = input().lower()

    if word[0] not in d or d[word[0]] != 0:
        return "NO"

    curr = 0

    for letter in word:
        if letter not in d:
            return "NO"
        if d[letter] != curr:
            if d[letter] == curr + 1:
                curr += 1
            else:
                return "NO"

    if curr == 3:
        return "YES"

    return "NO"


out = []
d = { "m":0, "e":1, "o":2, "w":3}

for _ in range(int(input())):
    out.append(main())

print("\n".join(map(str, out)))
