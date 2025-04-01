# https://www.acmicpc.net/problem/1389
# 케빈 베이컨의 6단계 법칙
# 
# 

import sys

input = sys.stdin.readline
n, m = map(int, input().strip().split())

INF = int(1e9)

mat = [[INF]*(n+1) for _ in range(n+1)]