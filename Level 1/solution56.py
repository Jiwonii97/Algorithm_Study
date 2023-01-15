# 코딩테스트 연습 / 연습문제 / 콜라 문제

def solution(a, b, n):
    answer = 0

    while n >= a:
        d, v = divmod(n, a)

        n = d*b+v
        answer += d*b

    return answer


print(solution(2, 1, 20))       # 19
print(solution(3, 1, 20))       # 9
print(solution(3, 2, 20))       # 18
