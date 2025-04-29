# https://www.acmicpc.net/problem/11286
# 절댓값 힙
# 우선순위큐, heapq 라이브러리를 이용해 자동정렬 진행, 원소의 경우 (절댓값, 기본값)으로 넣어 알아서 같이 정렬되게 작업
# O(logN)

import sys
import heapq

input = sys.stdin.readline
n = int(input().strip())

hq = []
for _ in range(n):
    x = int(input().strip())

    if x != 0:
        heapq.heappush(hq, (abs(x), x))
    else:
        if hq:
            print(heapq.heappop(hq)[1])
        else:
            print(0)
