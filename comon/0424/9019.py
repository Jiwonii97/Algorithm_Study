# https://www.acmicpc.net/problem/9019
# DSLR
# BFS, PyPy3로는 통과한다, 그냥 알고리즘 방식만 가져가면 될거 같다.
# O(V + E)

import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    start, end = map(int, input().split())

    visited = [False] * 10000
    dq = deque([(start, "")])
    visited[start] = True

    while dq:
        now, path = dq.popleft()

        # 1. D: 두 배, 10000 넘으면 나머지
        d = (now * 2) % 10000
        if not visited[d]:
            if d == end:
                print(path + "D")
                break
            visited[d] = True
            dq.append((d, path + "D"))

        # 2. S: 하나 줄이기, 0이면 9999
        s = 9999 if now == 0 else now - 1
        if not visited[s]:
            if s == end:
                print(path + "S")
                break
            visited[s] = True
            dq.append((s, path + "S"))

        # 3. L: 왼쪽 회전 (0343 → 3430)
        l = (now % 1000) * 10 + (now // 1000)
        if not visited[l]:
            if l == end:
                print(path + "L")
                break
            visited[l] = True
            dq.append((l, path + "L"))

        # 4. R: 오른쪽 회전 (0343 → 3034)
        r = (now % 10) * 1000 + (now // 10)
        if not visited[r]:
            if r == end:
                print(path + "R")
                break
            visited[r] = True
            dq.append((r, path + "R"))
