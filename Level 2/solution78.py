# 코딩테스트 연습 / 연습문제 / 연속 부분 수열 합의 개수


def solution(elements):
    answer = set()
    circular_words = elements*2

    for size in range(1, len(elements)+1):
        answer.update(set([sum(circular_words[i:i+size])
                           for i in range(len(elements))]))

    return len(answer)


print(solution([7, 9, 1, 1, 4]))         # 18
