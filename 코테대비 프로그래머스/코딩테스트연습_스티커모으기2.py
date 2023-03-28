# https://school.programmers.co.kr/learn/courses/30/lessons/12971
'''
    dq 문제
    처음을 했을때와 안했을때 2개를 큰 분류로 나눠서 탐색 진행
'''


def solution(sticker):
    if len(sticker) <= 3:
        return max(sticker)

    firstSticker, nofirstSticker = [0]*len(sticker), [0]*len(sticker)

    # 첫번째 스티커를 뜯은 경우
    firstSticker[0] = sticker[0]
    firstSticker[1] = sticker[0]

    for idx in range(2, len(sticker)-1):
        firstSticker[idx] = max(firstSticker[idx-2] +
                                sticker[idx], firstSticker[idx-1])

    # 첫번째 스티커를 뜯지 않은 경우
    for idx in range(1, len(sticker)):
        nofirstSticker[idx] = max(nofirstSticker[idx-2] +
                                  sticker[idx], nofirstSticker[idx-1])

    return max(firstSticker[-2], nofirstSticker[-1])


print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
print(solution([1, 3, 2, 5, 4]))
