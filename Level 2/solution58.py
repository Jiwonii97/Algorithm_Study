# 코딩테스트 연습 / 2018 KAKAO BLIND RECRUITMENT / [1차] 프렌즈4블록
# 단순 구현 문제, 중간중간 놓칠 만한 부분을 캐치하여 수정하는 것이 포인트, 마지막에 join과 list comprehension을 사용해 결과 출력
# 특히 카카오 코테를 보면 이와 같이 시간은 많이 소비되는 구현 문제가 나오곤 한다,
# 실수가 나지 않도록 작업을 진행한다면 크게 문제는 없을 거 같다.

def solution(m, n, board):    
    board = [list(b) for b in board]
    pos = [[1,0], [0,1], [1,1]]
    
    task = []
    while True:
        # 탐색
        for i in range(m-1):
            for j in range(n-1):
                target = board[i][j]
                if target == '*':
                    continue
                for p in pos:
                    [row, col] = p
                    if target != board[i+row][j+col]: break
                else:
                    task.append([i,j])
        
        # 더이상 작업할 공간이 없는 경우
        if len(task) == 0:
            break
        
        else:
            # 없어질 좌표를 -1로 지정
            for t in task:
                [i,j] = t
                board[i][j] = '*'
                
                for p in pos:
                    [row, col] = p
                    board[i+row][j+col] = '*'

            # 정리
            for i in range(1,m):
                for j in range(n):
                    if board[i][j] == '*':
                        for ii in range(i,0,-1):
                            board[ii][j] = board[ii-1][j]
                        board[0][j] = '*'

        task = []
          
    res = ''.join([''.join(b) for b in board])
        
    return res.count('*')

print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))           # 14
print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))           # 15