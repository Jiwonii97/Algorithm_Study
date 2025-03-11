import sys

n = int(sys.stdin.readline().strip())
number = list(map(int, sys.stdin.readline().strip().split()))

count = 1
prev = number[0]
for num in number[1:]:
    if prev == num:
        count += 1
    else:
        prev = num
        count = 1

    if count == 3:
        print("Yes")
        break
else:
    print("No")
