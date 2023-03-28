# https://school.programmers.co.kr/learn/courses/30/lessons/131704
'''
    단순 deque, stack 문제
'''


def solution(order):
    from collections import deque
    answer = 0

    conveyBelt = deque(range(1, len(order)+1))
    st = []

    for o in order:
        if o in st:     # 스택에 있는지 확인
            if o == st[-1]:
                st.pop()
                answer += 1
                continue
            else:
                break

        # 없으면 컨테이너 벨트에서 찾는다
        while conveyBelt:
            box = conveyBelt.popleft()
            if box == o:
                answer += 1
                break
            else:
                st.append(box)

    return answer


print(solution([4, 3, 1, 2, 5]))
print(solution([5, 4, 3, 2, 1]))
