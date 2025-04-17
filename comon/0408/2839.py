# https://www.acmicpc.net/problem/2839
# 설탕 배달
# 그리디+수학, 3의 갯수를 점차 늘려가면서 5가 가질 수 있는 최대값을 구해가면서 count 진행
# O(N)

import sys
input = sys.stdin.readline

n = int(input().strip())
count = n
n3 = 0
while n3*3 <= n:
    temp = n-n3*3
    if temp % 5 == 0:
        count = min(count, n3+temp//5)
    n3 += 1

print(count if count != n else -1)
