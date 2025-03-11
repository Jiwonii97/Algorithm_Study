# input() = sys.stdin.readline()

import sys

n = int(sys.stdin.readline().strip())

numbers = list(map(int, sys.stdin.readline().strip().split()))

prev = numbers[0]
for number in numbers[1:]:
    if prev >= number:
        print("No")
        break
    prev = number
else:
    print("Yes")
