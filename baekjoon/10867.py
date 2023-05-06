# https://www.acmicpc.net/problem/10867
# 중복 빼고 정렬하기

import sys

_ = sys.stdin.readline()
nums = sorted(set(map(int, sys.stdin.readline().split())))
for n in nums:
    print(n, end = " ")