# https://www.acmicpc.net/problem/15663
# N과 M (9)
# 수학, 순열 함수를 사용하여 문제풀이 진행
# O(NlogN)

import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().strip().split())
num = list(map(int, input().strip().split()))

outputs = sorted(set(permutations(num, m)))
for output in outputs:
    for o in output:
        print(o, end=" ")
    print()