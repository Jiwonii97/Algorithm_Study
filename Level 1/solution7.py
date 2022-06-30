# 코딩테스트 연습 / 2019 카카오 개발자 겨울 인턴십 / 크레인 인형뽑기 게임

def solution(board, moves):
    answer = 0
    _size = len(board)
    result = []
        
    for num in moves:
        for idx in range(_size):
            if board[idx][num-1] != 0:
                if len(result) != 0 and result[-1] == board[idx][num-1]:
                    answer += 2
                    result = result[:-1] # result.pop(-1), result.pop(-2)
                    # pop을 통해 리스트 원소 제거
                    board[idx][num-1] = 0
                else:
                    result.append(board[idx][num-1])
                    board[idx][num-1] = 0
                    
                break
    
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))