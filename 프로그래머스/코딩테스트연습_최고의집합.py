# https://school.programmers.co.kr/learn/courses/30/lessons/12938

def solution(n, s):
    if n > s:
        return [-1]

    m, v = divmod(s, n)

    answer = [m]*n

    for i in range(n-v, n):
        answer[i] += 1

    return answer


print(solution(2, 9))
print(solution(2, 1))
print(solution(2, 8))
