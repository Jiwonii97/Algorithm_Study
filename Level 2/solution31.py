# 코딩테스트 연습 / 깊이/너비 우선 탐색(DFS/BFS) / 게임 맵 최단거리
# deque를 이용해 하나씩 좌표를 뽑아서 해당 부분을 확인해 나가는 방식의 BFS 문제
# 좌표를 따질때 가로/세로 크기를 확실하게 확인할 것!!

from collections import deque

def solution(maps):
    points = [(-1,0),(0,1),(1,0),(0,-1)]     # [좌,상,우,하]
    n, m = len(maps), len(maps[0])
    maze_path = [[-1 for _ in range(m)] for _ in range(n)]
    maze_path[0][0] = 1
    
    # 길찾기를 진행할때 사용할 계산값 리스트
    dq = deque(); dq.append([0,0]) 
    while dq:
        [xpos, ypos] = dq.popleft()
        
        # 현재 위치를 기준으로 4방향의 위치 확인
        for point in points:
            nx, ny = xpos+point[0], ypos+point[1]
            
            # 조건에 맞는 경우
            if (0<=nx<n and 0<=ny<m) and maps[nx][ny] == 1:
                if maze_path[nx][ny] == -1:
                    maze_path[nx][ny] = maze_path[xpos][ypos] + 1
                    dq.append([nx,ny])
        
    return maze_path[-1][-1]

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))  # 11
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))  # -1