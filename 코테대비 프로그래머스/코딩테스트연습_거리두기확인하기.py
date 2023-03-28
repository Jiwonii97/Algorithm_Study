# https://school.programmers.co.kr/learn/courses/30/lessons/81302

def check_distance(place):
    # 'P' 값의 좌표만 plist에 추가함.
    plist = [(y, x) for y in range(5) for x in range(5) if place[y][x] == 'P']

    # 각 좌표끼리 거리를 계산하고, 거리에 따라 거리두기 여부 판단
    for y, x in plist:
        for y2, x2 in plist:
            dist = abs(y-y2) + abs(x-x2)  # 맨해튼 거리
            if dist == 0 or dist > 2:  # 같은 좌표이거나 거리가 2이상인 경우 continue
                continue

            if dist == 1:  # 두 사람 사이의 거리가 1인 경우
                return 0
            # 열이 같으나 두 사람 사이에 파티션이 없는 경우
            elif y == y2 and place[y][(x+x2)//2] != 'X':
                return 0
            # 행이 같으나 두 사람 사이에 파티션이 없는 경우
            elif x == x2 and place[(y+y2)//2][x] != 'X':
                return 0
            elif y != y2 and x != x2:  # 열/행이 다른경우(대각선), 두 사람 사이 파티션이 없는 경우
                if place[y2][x] != 'X' or place[y][x2] != 'X':
                    return 0
    return 1


def solution(places):
    answer = []
    # 각 place들을 check_distance함수로 조사
    for place in places:
        answer.append(check_distance(place))
    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP",
      "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))


'''
    from collections import deque

    def bfs(p):
        start = []
        
        for i in range(5): # 시작점이 되는 P 좌표 구하기
            for j in range(5):
                if p[i][j] == 'P':
                    start.append([i, j])
        
        for s in start:
            queue = deque([s])  # 큐에 초기값
            visited = [[0]*5 for i in range(5)]   # 방문 처리 리스트
            distance = [[0]*5 for i in range(5)]  # 경로 길이 리스트
            visited[s[0]][s[1]] = 1
            
            while queue:
                y, x = queue.popleft()
            
                dx = [-1, 1, 0, 0]  # 좌우
                dy = [0, 0, -1, 1]  # 상하

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0<=nx<5 and 0<=ny<5 and visited[ny][nx] == 0:
                        
                        if p[ny][nx] == 'O':
                            queue.append([ny, nx])
                            visited[ny][nx] = 1
                            distance[ny][nx] = distance[y][x] + 1
                        
                        if p[ny][nx] == 'P' and distance[y][x] <= 1:
                            return 0
        return 1


    def solution(places):
        answer = []
        
        for i in places:
            answer.append(bfs(i))
        
        return answer
'''
