# https://www.acmicpc.net/problem/10814
# 나이순 정렬
# 정렬 문제, lambda를 활용한 custom sort 진행 (O(NlogN))

import sys

n = int(sys.stdin.readline().strip())

a = []
for _ in range(n):
    age, name = sys.stdin.readline().strip().split()
    a.append((int(age), name))

a.sort(key=lambda x: x[0])

for aa in a:
    print(aa[0], aa[1])
