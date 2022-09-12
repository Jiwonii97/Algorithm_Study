# 코딩테스트 연습 / 월간 코드 챌린지 시즌3 / n^2 배열 자르기
# 표를 통해 직접 규칙을 발견하고 이를 적용하는 단순 수학 구현 문제이다.
# 이런 풀이 방법을 처음에는 생각하기 어려우니 자주 접하면서 여러 시각으로 문제를 접근하는 것이 좋아보임(좌표값을 이용하여 계산을 할 것이라 생각을 못함)

def solution(n, left, right):
    answer = []
    
    for number in range(left, right+1):
        div, mod = divmod(number, n)
        answer.append(max(div, mod)+1)
    
    return answer

print(solution(3,2,5))          # 	[3,2,2,3]
print(solution(4,7,14))         # 	[4,3,3,3,4,4,4,4]

'''
    < 처음 풀이 >
    # n^2번을 2중 for문을 실행하니 시간초과가 발생
    def solution(n, left, right):
        answer = []
        for i in range(1, n+1):
            for j in range(1, n+1):
                inputNum = i if i>j else j
                answer.append(inputNum)
        
        return answer[left:right+1]
'''