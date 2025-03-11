import sys

n, m = map(int, sys.stdin.readline().strip().split())

bs = sorted(map(int, sys.stdin.readline().strip().split()))[::-1]
ws = sorted(map(int, sys.stdin.readline().strip().split()))[::-1]

output = 0
for idx in range(len(bs)):
    b = bs[idx]
    w = ws[idx] if idx < len(ws) else 0

    if b <= 0:      # b가 음수일때
        if b+w >= 0:
            output += b+w
    else:       # b가 양수일때
        if w < 0:
            output += b
        else:
            output += (b+w)


print(output)
