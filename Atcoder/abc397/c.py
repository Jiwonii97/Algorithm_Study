import sys

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))

output = 0
for i in range(1, len(a)):
    x, y = set(a[:i]), set(a[i:])

    output = max(output, len(x)+len(y))

print(output)
