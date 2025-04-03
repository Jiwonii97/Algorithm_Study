# https://www.acmicpc.net/problem/1003
# 피보나치 함수
# DP, 피보나치는 결국 마지막 2개를 계속 계산하는 점화식을 가지기 때문에 DP에 적합, 0과 1의 개수를 같이 저장하여 갱신시키며 값을 미리 구하고 한번에 계산
# O(T)

import sys

input = sys.stdin.readline

t = int(input().strip())
fibo = [(1, 0), (0, 1)]
for _ in range(40):
    f1, f2 = fibo[-2], fibo[-1]
    fibo.append((f1[0]+f2[0], f1[1]+f2[1]))
for _ in range(t):
    n = int(input().strip())
    print(f"{fibo[n][0]} {fibo[n][1]}")