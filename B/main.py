""" Solves Problem B"""

import sys

sys.stdin = open('B/input.txt', 'r', encoding="utf8")
input = lambda: sys.stdin.readline().rstrip()

def main(string: str, k: int) -> str:
    """ Main Function """

    big = [0]*26
    small = [0]*26

    for letter in string:

        letter = ord(letter)

        if letter >= ord("a"):
            small[letter - ord("a")] += 1
        else:
            big[letter - ord("A")] += 1

    result = 0

    for i in range(26):

        pairs = min(small[i], big[i])

        result += pairs

        if k:
            extras = abs(big[i] - small[i]) // 2
            result += min(extras, k)
            k = max(k-extras, 0)

    return result

out = []

for _ in range(int(input())):
    length, k_str = input().split(" ")
    input_string = input()
    out.append( main(input_string, int(k_str)) )

print("\n".join(map(str, out)))
