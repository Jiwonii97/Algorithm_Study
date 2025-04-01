# https://www.acmicpc.net/problem/15829
# Hashing
# list comprehension을 응용한 계산 문제, 처음 문제를 이해하는데 다소 어려움은 있었지만 큰 어려움은 없었음
# O(N)

import sys

input = sys.stdin.readline

r = 31
m = 1234567891
eng_dict = {c:idx for idx, c in enumerate(list("abcdefghijklmnopqrstuvwxyz"), start=1)}

l = int(input().strip())
texts = list(input().strip())

output = sum([eng_dict[text]*(r**idx) for idx, text in enumerate(texts)])%m

print(output)
