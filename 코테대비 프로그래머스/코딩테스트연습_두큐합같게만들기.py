# https://school.programmers.co.kr/learn/courses/30/lessons/118667

def solution(queue1, queue2):
    from collections import deque
    answer = 0

    q1 = deque(queue1)
    q2 = deque(queue2)
    limit = 4*len(queue1)
    total1 = sum(queue1)
    total2 = sum(queue2)

    while True:
        if total1 < total2:
            tgt = q2.popleft()
            q1.append(tgt)
            total1 += tgt
            total2 -= tgt
        elif total1 > total2:
            tgt = q1.popleft()
            q2.append(tgt)
            total1 -= tgt
            total2 += tgt
        else:
            break

        answer += 1

        if answer == limit:
            answer = -1
            break

    return answer


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1, 1], [1, 5]))
