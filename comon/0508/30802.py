# https://www.acmicpc.net/problem/30802
# 웰컴 키트
# 수학, divmod 함수 활용 나머지 계산 문제
# O(n)

import sys
input = sys.stdin.readline

n = int(input().strip())
tshirts = list(map(int, input().strip().split()))
t, p = map(int, input().strip().split())

tss = 0
for ts in tshirts:
    tm, tv = divmod(ts, t)
    tss += (tm + (tv>0))
print(tss)

m, v = divmod(n, p)
print(f"{m} {v}")