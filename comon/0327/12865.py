# https://www.acmicpc.net/problem/12865
# 평범한 배낭
# knapsack 문제(DP), 이전까지의 weight를 계산하여 다음 값을 예상
# O(VW)


import sys

input = sys.stdin.readline
n, k = map(int, input().split())
backpacks = sorted([list(map(int, input().split())) for _ in range(n)], key = lambda x: x[0])

dp = [[0]*(k+1) for _ in range(n+1)]      # dp 초기값

for i, backpack in enumerate(backpacks):
    for j in range(k+1):
        weight, value = backpack        # 무게, 가치

        if j < weight:      # 가방 무게가 해당 경우에서 가능하지 않으면
            dp[i+1][j] = dp[i][j]
        else:               # 이전 데이터들을 기반으로 가능한지 확인
            dp[i+1][j] = max(dp[i][j], dp[i][j-weight] + value)

print(dp[n][k])