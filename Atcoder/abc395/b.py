n = int(input())

grid = [['.' for _ in range(n)] for _ in range(n)]

for i in range(n):
    s = []
    for j in range(n):
        print(i, j, n-1-i, n-1-j)
        x = min(i, j, n-1-i, n-1-j)
        if x % 2:  # odd
            s.append('.')
        else:  # even
            s.append('#')

    print(''.join(s))
