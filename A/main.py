import sys

sys.stdin = open('input.txt', 'r')
input = lambda: sys.stdin.readline().rstrip()

def solve():

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
    out.append(solve())

print("\n".join(map(str, out)))