# https://www.acmicpc.net/problem/2108
# 통계학
# 정렬/구현, Counter 함수 응용 최빈값 계산 방식, 음수 고려 반올림 커스텀 함수
# Counter() -> 원소 빈도에 대한 Dict (values, items, keys)
# 음수 고려 반올림 함수

import sys
from collections import Counter

def my_round(n):
    return int(n + 0.5) if n > 0 else int(n - 0.5)

input = sys.stdin.readline

n = int(input().strip())
nums = sorted([int(input().strip()) for _ in range(n)])

print(my_round(sum(nums)/len(nums)))     # 산술평균
print(nums[len(nums)//2])       # 중앙값

common = Counter(nums)
max_count = max(common.values())
filterd_common = sorted([k for k, v in common.items() if v == max_count])
print(filterd_common[1] if len(filterd_common)>1 else filterd_common[0])        # 최빈값

print(nums[-1]-nums[0])         # 범위
# print(max(nums)-min(nums))         # 범위