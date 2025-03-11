# https://www.acmicpc.net/problem/2805
# 나무 자르기 (O(NlogN))
# 이분 탐색

import sys

n, m = map(int, sys.stdin.readline().strip().split())
trees = list(map(int, sys.stdin.readline().strip().split()))

start, end = 0, max(trees)
while start <= end:
    mid = (start+end)//2

    count = sum([max(0, tree-mid) for tree in trees])

    if m <= count:
        start = mid+1
    else:
        end = mid-1

print(end)