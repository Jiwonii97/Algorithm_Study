# https://www.acmicpc.net/problem/1874
# 스택 수열
# 단순 스택 구현 문제, 입력과 함께 구하는 것이 시간단축의 포인트

import sys

# N 입력
n = int(sys.stdin.readline().strip())

stack = []
result = []
point = 1

for _ in range(n):
    current = int(sys.stdin.readline().strip())     # 찾을 숫자 입력
    
    while current >= point:
        stack.append(point)     # 일단 push
        result.append('+')
        point += 1
    
    if current == stack[-1]:         # 마지막에 넣은 것이 구해야 하는 순열과 같은 경우, 다른게 나올때 까지 반복
        stack.pop()
        result.append('-')
    else:
        result = ["NO"]
        break

print('\n'.join(result))