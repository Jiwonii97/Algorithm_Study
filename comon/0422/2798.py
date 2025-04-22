# https://www.acmicpc.net/problem/2798
# 블랙잭
# 수학, 조합+정렬 문제, 조건에 맞는 정렬 진행

import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().strip().split())

cards = combinations(list(map(int, input().strip().split())), 3)
cases = sorted([(m-sum(c), sum(c)) for c in cards if sum(c) <= m], key=lambda x : x[0])

print(cases[0][1])
