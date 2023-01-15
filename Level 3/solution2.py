# 코딩테스트 연습 / 깊이/너비 우선 탐색(DFS/BFS) / 단어 변환

from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0

    dq = deque()
    dq.append([begin, 0])

    while dq:
        curWord, idx = dq.popleft()
        if curWord == target:
            return idx

        for curTarget in words:
            diff = 0
            for c, t in zip(curWord, curTarget):
                if c != t:
                    diff += 1

                if diff > 1:
                    break
            if diff == 1:
                dq.append([curTarget, idx+1])

    return 0


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
