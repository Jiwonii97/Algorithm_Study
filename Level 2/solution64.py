# 코딩테스트 연습 / 월간 코드 챌린지 시즌1 / 삼각 달팽이
# 나머지 연산과 2차원 배열의 좌표과의 규칙을 확인해 문제 풀이, 2차원 배열 -> 1차원 배열로 바꿀수 있는 방법을 익힘

def solution(n):
    answer = [[-1 for _ in range(i)] for i in range(1,n+1)]
    
    [i, j], tgt = [-1,0], 0
    for k in range(n):
        # 밑으로 이동
        if k%3==0:
            for _ in range(n-k):
                tgt, i = tgt+1, i+1
                answer[i][j] = tgt
        # 우로 이동
        elif k%3==1:
            for _ in range(n-k):
                tgt, j = tgt+1, j+1
                answer[i][j] = tgt
        # 대각선으로 이동
        elif k%3==2:
            for _ in range(n-k):
                tgt, i, j = tgt+1, i-1, j-1
                answer[i][j] = tgt
    
    answer = [line for lines in answer for line in lines if line != -1]
    # sum(answer, []) : 2차원의 배열을 1차원으로 변환
    
    return answer

print(solution(4))          # [1,2,9,3,10,8,4,5,6,7]
print(solution(5))          # [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
print(solution(6))          # [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]