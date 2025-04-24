# https://www.acmicpc.net/problem/10773
        

# 제로
# 단순 스택 문제
# O(N)

import sys
input = sys.stdin.readline

k = int(input().strip())

stack = []
for _ in range(k):
    n = int(input().strip())

    if stack and n==0:
        stack.pop()
    else:
        stack.append(n)
else:
    print(sum(stack))