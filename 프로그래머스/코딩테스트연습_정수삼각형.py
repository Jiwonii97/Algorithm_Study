# https://school.programmers.co.kr/learn/courses/30/lessons/43105
# 코딩테스트 연습 / 동적계획법(Dynamic Programming) / 정수 삼각형

def solution(triangle):
    maxLen = len(triangle)

    for i in range(1, maxLen):
        for j in range(i+1):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])

    return max(triangle[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
