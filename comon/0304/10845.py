# https://www.acmicpc.net/problem/10845
# 큐
# 큐 구조의 이해
# TIL: `input()`보다 `sys.stdin.readline()`가 더 시간이 적게 듬

import sys
from collections import deque

n = int(sys.stdin.readline())

dq = deque()
for _ in range(n):
    tasks = sys.stdin.readline().strip().split()
    if tasks[0] == "push":
        dq.append(tasks[1])
    elif tasks[0] == "pop":
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif tasks[0] == "size":
        print(len(dq))
    elif tasks[0] == "empty":
        print(0 if len(dq) else 1)
    elif tasks[0] == "front":
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif tasks[0] == "back":
        if dq:
            print(dq[-1])
        else:
            print(-1)
