# https://www.acmicpc.net/problem/9095
# 1, 2, 3 더하기
# DP, 점화식 활용 문제 풀이
# O(N)

import sys
input = sys.stdin.readline

t = int(input().strip())
arr = [0] * 11
arr[1] = 1
arr[2] = 2
arr[3] = 4

for i in range(4,11):
    arr[i] = arr[i-1] + arr[i-2] + arr[i-3]

for _ in range(t):
    n = int(input())
    print(arr[n])
