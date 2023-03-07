# https://school.programmers.co.kr/learn/courses/30/lessons/138476

def solution(k, tangerine):
    from collections import Counter
    answer = 0

    cases = Counter(tangerine).most_common()

    while cases:
        tg = cases.pop(0)
        k -= tg[1]
        answer += 1

        if k <= 0:
            break

    return answer


print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))
