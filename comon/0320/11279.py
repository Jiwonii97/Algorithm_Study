# https://www.acmicpc.net/problem/11279
# 최대 힙
# heapq는 최소 합만을 지원한다. 이에 입력 값에 음수를 취하면 반대로 최대 힙을 구할 수 있다.
# O(NlogN)

import sys
import heapq

n = int(sys.stdin.readline().strip())

dq = []
for _ in range(n):
    num = int(sys.stdin.readline().strip())

    if num == 0:
        if dq:
            o = -heapq.heappop(dq)
        else:
            o = 0
        print(o)
    else:
        heapq.heappush(dq, -num)
