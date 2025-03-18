# www.acmicpc.net/problem/1149
# RGB 거리
# DP 문제 / 3가지 케이스를 두어 각 케이스를 시작함에 따라 나오는 결과값의 최솟값을 사용 (O(n))

import sys

n = int(sys.stdin.readline().strip())

house = []
for _ in range(n):
    r, g, b = map(int, sys.stdin.readline().strip().split())
    house.append([r, g, b])

dp = [[0] * 3 for _ in range(n)]
dp[0] = house[0]

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + house[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + house[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + house[i][2]

print(min(dp[n-1]))
