# 코딩테스트 연습 / 연습문제 / 둘만의 암호

def solution(s, skip, index):
    answer = ''
    WORD = "abcdefghijklmnopqrstuvwxyz"
    for sk in skip:
        WORD = WORD.replace(sk, "")
    length = len(WORD)

    for ss in s:
        idx = WORD.index(ss)
        answer += WORD[(idx+index) % length]

    return answer


print(solution("aukks", "wbqd", 5))
