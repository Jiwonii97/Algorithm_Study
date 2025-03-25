# https://www.acmicpc.net/problem/10989
# 수 정렬하기 3
# 일반적인 정렬(sort)를 활용할 수 없는 문제, 메모리 사용을 최소로 하기 위해 리스트를 응용해 해당 숫자가 몇개가 있는지 확인, 이후 숫자가 있는 경우에만 가져와 사용
# O(N)

import sys

n = int(sys.stdin.readline().strip())

arr = [0]*10101
for _ in range(n):
    num = int(sys.stdin.readline().strip())
    arr[num] += 1

for idx, a in enumerate(arr):
    for _ in range(a):
        print(idx)
