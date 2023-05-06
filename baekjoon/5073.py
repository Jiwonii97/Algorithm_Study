# https://www.acmicpc.net/problem/5073
# 삼각형과 세변

import sys

while True:
    tries = list(map(int, sys.stdin.readline().split()))
    if tries == [0,0,0]:  break
    
    max_len = max(tries)
    tries.remove(max_len)
    if max_len >= sum(tries):
        print("Invalid")
        continue
    
    tries.append(max_len)
    
    if len(set(tries)) == 1:
        print("Equilateral")
    elif len(set(tries)) == 2:
        print("Isosceles")
    elif len(set(tries)) == 3:
        print("Scalene")