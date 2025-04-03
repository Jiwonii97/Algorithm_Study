# https://www.acmicpc.net/problem/11053
# 가장 긴 증가하는 부분 수열
# DP, LIS 문제, 이전 갑소가 비교해 나가면서 count 진행
# O(N^2)

import sys

input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().strip().split()))

dp = [1]*n
for i in range(1, n):
    for j in range(i):
        if arr[j]<arr[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

print(max(dp))