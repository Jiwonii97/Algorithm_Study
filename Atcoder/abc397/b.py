# 단순 String 문제, 규칙성을 발견하고 규칙 마다의 경우를 확인

import sys

ss = list(sys.stdin.readline().strip())
result = 0

while ss:
    # i, o
    if len(ss) == 1:
        result += 1
        del ss[:1]
    elif ss[:2] == ["i", "o"]:
        del ss[:2]
    else:
        result += 1
        del ss[:1]

print(result)
