# 코딩테스트 연습 / 2018 KAKAO BLIND RECRUITMENT / [3차] 압축
# 리스트와 딕셔너리 활용 문제, 연속적인 문자열을 이용한다는 점에서 쉽게 접근가능했음, 한두개 풀이를 해가며 접근하는 방식이 중요한듯

def solution(msg):
    answer = []
    Alpabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    indexes = {x:i+1 for i, x in enumerate(Alpabet)}
    
    nextIdx = 27
    
    word = ""
    msg = list(msg)
    while msg:
        # 걸러낼 단어 생성기
        while True:
            word += msg.pop(0)
            # 더이상 골라낼 단어가 없음
            if len(msg) == 0:
                break
            # 해당 단어는 딕셔너리에 있고, 다음꺼를 포함한 것은 딕셔너리에 없으면 추가를 하고 작업 수행
            elif word in indexes.keys() and (word + msg[0]) not in indexes.keys():
                indexes[word + msg[0]] = nextIdx
                nextIdx += 1
                break
        
        # 현재 단어는 들어가지만 다음 단어까지 포함하면 안되는 경우
        answer.append(indexes[word])
        word = ""       # 초기화
    
    return answer


print(solution("KAKAO"))            # 	[11, 1, 27, 15]
print(solution("TOBEORNOTTOBEORTOBEORNOT"))         # 	[20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
print(solution("ABABABABABABABAB"))         # 	[1, 2, 27, 29, 28, 31, 30]


'''
    < 다른 풀이 >
    # 비슷한 방식으로 문제 풀이를 접근하였지만, 문자열을 slicing 하며 업데이트를 한점, __len__(), chr(e+64)라는 아스키코드 값을 활용한 점에서 괜찮은 방법이라 생각한다
    def solution(msg):
        answer = []
        tmp = {chr(e + 64): e for e in range(1, 27)}
        num = 27
        while msg:
            tt = 1
            while msg[:tt] in tmp.keys() and tt <= msg.__len__():
                tt += 1
            tt -= 1
            if msg[:tt] in tmp.keys():
                answer.append(tmp[msg[:tt]])
                tmp[msg[:tt + 1]] = num
                num += 1
            msg = msg[tt:]
        return answer
'''