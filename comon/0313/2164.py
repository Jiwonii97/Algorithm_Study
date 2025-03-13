# https://www.acmicpc.net/problem/2164
# 카드2
# 시간 복잡도 : O(n)

import sys
from collections import deque

n = int(sys.stdin.readline().strip())
deque = deque([i for i in range(1, n + 1)])

while len(deque) > 1:
    card1 = deque.popleft()
    deque.append(deque.popleft())

print(deque[0])
