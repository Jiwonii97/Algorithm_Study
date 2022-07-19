# 코딩테스트 연습 / 2021 Dev-Matching: 웹 백엔드 개발자(상반기) / 행렬 테두리 회전하기
# 큐를 이용해 노가다로 품, 근데 다 비슷한게 푼듯

def solution(rows, columns, queries):
    answer = []
    arr = [[y for y in range(x,x+columns)] for x in range(1,columns*rows+1,columns)]
    
    for query in queries:
        [x1, y1, x2, y2] = query
        q = []
        
        for ypos in range(y1-1,y2):
            q.append(arr[x1-1][ypos])
        for xpos in range(x1,x2):
            q.append(arr[xpos][y2-1])
        for ypos in range(y2-2,y1-2,-1):
            q.append(arr[x2-1][ypos])
        for xpos in range(x2-2,x1-1,-1):
            q.append(arr[xpos][y1-1])
            
        q.insert(0,q.pop())
        answer.append(min(q))
        
        # 다시 삽입
        idx = 0
        for ypos in range(y1-1,y2):
            arr[x1-1][ypos] = q[idx]
            idx += 1
        for xpos in range(x1,x2):
            arr[xpos][y2-1] = q[idx]
            idx += 1
        for ypos in range(y2-2,y1-2,-1):
            arr[x2-1][ypos] = q[idx]
            idx += 1
        for xpos in range(x2-2,x1-1,-1):
            arr[xpos][y1-1] = q[idx]
            idx += 1
            
    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
print(solution(100,97,[[1,1,100,97]]))

'''
    < 다른 풀이 >
    from collections import deque
    def solution(rows, columns, queries):
        arr = [[i+columns*j for i in range(1,columns+1)] for j in range(rows)]
        answer, result = deque(), []
        for i in queries:
            a,b,c,d = i[0]-1,i[1]-1,i[2]-1,i[3]-1
            for x in range(d-b):
                answer.append(arr[a][b+x])
            for y in range(c-a):
                answer.append(arr[a+y][d])
            for z in range(d-b):
                answer.append(arr[c][d-z])
            for k in range(c-a):
                answer.append(arr[c-k][b])
            answer.rotate(1)
            result.append(min(answer))
            for x in range(d-b):
                arr[a][b+x] = answer[0]
                answer.popleft()
            for y in range(c-a):
                arr[a+y][d] = answer[0]
                answer.popleft()
            for z in range(d-b):
                arr[c][d-z] = answer[0]
                answer.popleft()
            for k in range(c-a):
                arr[c-k][b] = answer[0]
                answer.popleft()
        return result
'''