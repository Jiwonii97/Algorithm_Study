# 코딩테스트 연습 / 연습문제 / 멀리 뛰기
# DP를 사용해 미리 파스칼 삼각형을 구하고 이를 활용해 문제 풀이

def solution(num):
    answer = 0

    # dp / comb[n][r] == nCr
    comb = [[0 for _ in range(num+1)] for _ in range(num+1)]
    for n in range(num+1):
        for r in range(num+1):
            # 파스칼 삼각형 구하기
            if n<r:
                continue

            if r==0 or n==r:
                comb[n][r] = 1
            else:
                comb[n][r] = comb[n-1][r] + comb[n-1][r-1]
    
    # 파스칼 삼각형을 사용해 문제 풀이
    n, r = num, 0
    
    while n>=r:
        answer += comb[n][r]
        n, r = n-1, r+1

    return answer%1234567

print(solution(4))      # 5
print(solution(3))      # 3