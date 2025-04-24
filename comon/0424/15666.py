# https://www.acmicpc.net/problem/15666
# N과 M (12)
# 그리드 / 중복조합 + 중복 처리
# O(n^m)

import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

n, m = map(int, input().strip().split())
numbers = sorted(set(map(int, input().strip().split())))

# 중복 제거용 set
seen = set()

for comb in combinations_with_replacement(numbers, m):
    if comb not in seen:
        seen.add(comb)
        print(*comb)
