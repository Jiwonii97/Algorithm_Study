# https://www.acmicpc.net/problem/1406
# 에디터

# 커서가 아닌 Stack을 이용한 풀이
import sys

words = sys.stdin.readline().strip()
size = int(sys.stdin.readline().strip())

dq1, dq2 = list(words), []

for _ in range(size):
    commands = sys.stdin.readline().split()
    if commands[0] == "L":
        if dq1: dq2.append(dq1.pop())
        else: continue
    elif commands[0] == "D":
        if dq2: dq1.append(dq2.pop())
        else: continue
    elif commands[0] == "B":
        if dq1: dq1.pop()
        else: continue
    elif commands[0] == "P":
        dq1.append(commands[1])
        

print(''.join(dq1+dq2[::-1]))
