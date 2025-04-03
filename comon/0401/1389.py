# https://www.acmicpc.net/problem/1389
# 케빈 베이컨의 6단계 법칙
# 
# 

import sys

input = sys.stdin.readline
n, m = map(int, input().strip().split())

friend_map = [[n]*(n) for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().strip().split())
    friend_map[x-1][y-1] = 1
    friend_map[y-1][x-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i==j:
                friend_map[i][j] = 0
            else:
                friend_map[i][j] = min(friend_map[i][j], friend_map[i][k]+friend_map[k][j])

friends = []
for row in friend_map:
    friends.append(sum(row))
print(friends.index(min(friends)) + 1)