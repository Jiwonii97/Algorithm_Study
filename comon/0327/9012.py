# https://www.acmicpc.net/problem/9012
# 괄호
# 간단한 스택 구현 문제, 새로운 입력값과 스택의 마지막 값을 확인했을때 괄호를 만족하면 pop
# O(TxN)

import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    dq = []
    lines = list(sys.stdin.readline().strip())

    for line in lines:
        if len(dq)<1:
            dq.append(line)
        else:
            if dq[-1]+line == "()":
                dq.pop()
            else:
                dq.append(line)
    else:
        print("NO" if dq else "YES")