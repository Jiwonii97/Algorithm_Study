# https://www.acmicpc.net/problem/1927
# 최소 힙
# 우선순위 큐를 적용한 자동적으로 정렬을 해주는 자료구조 연구 (O(NlogN))

import sys
import heapq

n = int(sys.stdin.readline().strip())
dq = []

for _ in range(n):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        if dq:
            print(heapq.heappop(dq))
        else:
            print(0)
    else:
        heapq.heappush(dq, x)
