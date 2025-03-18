# www.acmicpc.net/problem/11659
# 구간 합 구하기 4
# 누적합 (Prefix Sum) 
# 배열 또는 리스트 등에서 일정 구간의 합을 빠르게 계산하기 위한 방법이면서 동적 계획법(DP)의 형태 중 하나, 기본적인 방식은 각 요소까지의 누적 합을 계산하여 이를 배열에 저장해 두는 것
# 이후에 특정 구간의 합을 구할 때는 해당 구간의 끝 지점까지의 누적 합에서 시작 지점까지의 누적 합을 빼면서 계산, 해당 알고리즘은 배열 또는 리스트의 요소가 고정되어 있을 때 구간 합을 반복적으로 계산해야 하는 경우 유용하게 사용
# 시간 복잡도 (O(n))

import sys

n, m = map(int, sys.stdin.readline().strip().split())

# 누적합 배열 생성
arr = [0]
nums = map(int, sys.stdin.readline().strip().split())
for num in nums:
    arr.append(arr[-1] + num)

for _ in range(m):
    start, end = map(int, sys.stdin.readline().strip().split())
    print(arr[end] - arr[start-1])
