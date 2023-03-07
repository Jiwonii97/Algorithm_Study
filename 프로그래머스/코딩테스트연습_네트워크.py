# https://school.programmers.co.kr/learn/courses/30/lessons/43162
#  코딩테스트 연습 / 깊이/너비 우선 탐색(DFS/BFS) / 네트워크
'''
    BFS 활용
    -> 시작을 하고 하나씩 넣어 가면서 반복
'''


def solution(n, computers):
    answer = []
    network = {}

    for num1, computer in enumerate(computers):
        network[num1] = []
        for num2, c in enumerate(computer):
            if c == 1 and num1 != num2:
                network[num1].append(num2)

    for idx in range(n):
        for nw in answer:
            if idx in nw:
                break
        else:
            inputData = []
            q = [idx]
            while q:
                point = q.pop(0)
                if point not in inputData:
                    inputData.append(point)
                    nextNetwork = network[point]
                    q.extend(nextNetwork)

            answer.append(inputData)

    return len(answer)


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
