# https://www.acmicpc.net/problem/11650
# 좌표 정렬하기
# 정렬, 단순 lambda 함수 활용 정렬 문제
# O(NlogN)

import sys
input = sys.stdin.readline

n = int(input().strip())
num = sorted([list(map(int, input().strip().split())) for _ in range(n)], key=lambda x: (x[0], x[1]))

for nn in num:
    print(f"{nn[0]} {nn[1]}")