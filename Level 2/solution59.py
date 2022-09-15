# 코딩테스트 연습 / 연습문제 / 땅따먹기
# DP 문제, DP로 이전 행의 최대값을 개별적으로 구해 최종적으로 최댓값을 확인하는 방식

def solution(land):
    row, col = len(land), len(land[0])

    # DP활용
    for i in range(1,row):
        for j in range(col):
            land[i][j] += max(land[i-1][:j]+land[i-1][j+1:])

    return max(land[-1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))            # 16