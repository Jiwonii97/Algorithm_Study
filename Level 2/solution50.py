# 코딩테스트 연습 / 2017 팁스타운 / 예상 대진표
# 단순 구현 문제, 2를 곱하며 그 그룹 안에 같은 멤버가 있어야 한다는것을 확인 후 몫 연산을 활용한 방법

def solution(n,a,b):
    for g in range(1,n+1):
        if (a-1)//2**g == (b-1)//2**g:
            return g

print(solution(8,4,7))          # 3