# 코딩테스트 연습 / 연습문제 / 덧칠하기

def solution(n, m, section):
    answer = 0
    paint = 0

    for s in section:
        if s >= paint:
            paint = s+m
            answer += 1

    return answer


print(solution(8, 4, [2, 3, 6]))
print(solution(5, 4, [1, 3]))
print(solution(4, 1, [1, 2, 3, 4]))


'''
    def solution(n, m, section):
        answer = 0
        section = sorted(section)

        while section:
            tgt = section.pop(0)
            for i in range(tgt, tgt+m):
                if i in section:
                    section.remove(i)
            answer += 1

        return answer
'''
