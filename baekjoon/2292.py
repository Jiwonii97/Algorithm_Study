# https://www.acmicpc.net/problem/2292
# 벌집

import sys

_input = int(sys.stdin.readline().strip())
if _input == 1:
    print(1)
else:
    _input -= 1
    n, cnt = 6, 1
    while True:
        if _input <= n:
            break
        else:
            cnt += 1
            n += 6*cnt

    print(cnt+1)
