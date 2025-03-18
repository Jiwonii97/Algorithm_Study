# 단순 조건부 출력 구현 문제

import sys

x = float(sys.stdin.readline().strip())
print(1 if x >= 38.0 else (2 if 38.0 > x >= 37.5 else 3))
