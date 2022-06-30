# 코딩테스트 연습 / 월간 코드 챌린지 시즌1 / 내적
 
def solution(a, b):
    return sum(num1*num2 for num1, num2 in zip(a,b))

print(solution([1,2,3,4],[-3,-1,0,2]))
print(solution([-1,0,1],[1,0,-1]))