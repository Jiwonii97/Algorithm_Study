# 코딩테스트 연습 / 연습문제 / 하노이의 탑
# 하노이의 탑 기본 예제

def solution(n):
    answer = []
    
    def hanoi(froms, tos, subs, n):
        if n == 1:
            answer.append([froms, tos])
        else:
            hanoi(froms,subs,tos,n-1)       # n-1개를 일단 sub에 옮기고
            hanoi(froms,tos,subs,1)         # 제일 큰거를 to에 옮기고
            hanoi(subs,tos,froms,n-1)       # 남음 n-1개를 from을 sub로 두고 to로 옮기긱
            
    hanoi(1,3,2,n)
    
    return answer

print(solution(2))      # [ [1,2], [1,3], [2,3] ]