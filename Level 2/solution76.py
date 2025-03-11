# 코딩테스트 연습 / 연습문제 / 야근 지수 (아직 못품)

def solution(n, works):
    if sum(works) <= n:
        return 0

    for _ in range(n):
        tmp = []
        for idx in range(len(works)):
            num = 0
            for i, w in enumerate(works):
                if i == idx:
                    num += (w-1)**2
                else:
                    num += w ** 2
            tmp.append(num)
        works[tmp.index(min(tmp))] -= 1

    return sum([w**2 for w in works])


print(solution(4, [4, 3, 3]))
print(solution(1, [2, 1, 2]))
print(solution(3, [1, 1]))
