# https://school.programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[1][1] = 1        # 시작점 지정

    for i, j in puddles:  # 웅덩이 제거
        dp[j][i] = -1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if dp[i][j] == -1:      # 웅덩이인 이유
                dp[i][j] = 0
                continue

            dp[i][j] += (dp[i-1][j] + dp[i][j-1]) % 1000000007

    return dp[n][m]


print(solution(4, 3, [[2, 2]]))
