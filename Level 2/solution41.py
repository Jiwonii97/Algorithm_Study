# 코딩테스트 연습 / 연습문제 / 가장 큰 정사각형 찾기
# < DP 문제 > 
# 정사각형을 만들고 싶으면 이전 데이터의 위/왼위/왼을 보고 그 중 최솟값을 가져오면 확인 할 수 있다
# DP 문제를 푸는 방법에 대해 추가적으로 도전할 필요를 느낌

def solution(board):
        for i in range(1,len(board)):
            for j in range(1,len(board[0])):
                # 0이 아닐 때만 값 업데이트 / 0이면 포함시키지 않음
                if board[i][j] >= 1:
                    board[i][j] = min(board[i-1][j],board[i][j-1],board[i-1][j-1]) + 1
        return max([num for row in board for num in row])**2

# 출력
print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))      # 9
print(solution([[0,0,1,1],[1,1,1,1]]))          # 4

'''
    cf) [num for row in board for num in row] 이와 같이 list comprehension에 for 문을 두번 적용하면 앞의 for문이 먼저 나온다
'''