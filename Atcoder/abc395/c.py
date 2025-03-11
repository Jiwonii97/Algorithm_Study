import sys

n = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))

distance = int(1e6)
visited = [-1]*(10**6+1)
for idx in range(len(numbers)):
    if visited[numbers[idx]] != -1:
        distance = min(distance, idx-visited[numbers[idx]]+1)
    else:
        visited[numbers[idx]] = idx

print(distance if distance != int(1e6) else -1)
