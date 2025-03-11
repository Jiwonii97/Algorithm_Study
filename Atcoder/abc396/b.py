import sys

n = int(sys.stdin.readline().strip())

stack = [0]*n
for _ in range(n):
    tasks = list(map(int, sys.stdin.readline().strip().split()))

    if tasks[0] == 1:
        stack.append(tasks[1])
    elif tasks[0] == 2:
        print(stack.pop())
