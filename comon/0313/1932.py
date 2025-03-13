# https://www.acmicpc.net/problem/1932
# 정수 삼각형
# DP 구조를 적용한 문제 풀이 방식 (O(N^2))

import sys

n = int(sys.stdin.readline().strip())

# 삼각형 정보 입력
mat = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

# DP 방식을 응용한 최대값 구하기
for i in range(1, n):
    for j in range(len(mat[i])):
        # 삼각형 왼쪽 끝
        if j == 0:
            mat[i][j] += mat[i-1][j]
        # 삼각형 오른쪽 끝
        elif j == len(mat[i]) - 1:
            mat[i][j] += mat[i-1][j-1]
        # 삼각형 중간 부분
        else:
            mat[i][j] += max(mat[i-1][j-1], mat[i-1][j])

print(max(mat[-1]))
