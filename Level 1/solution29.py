# 코딩테스트 연습 / 연습문제 / 같은 숫자는 싫어

def solution(arr):
    answer = []
    for data in arr:
        if len(answer) == 0 or data != answer[-1]:
            answer.append(data)
    return answer

'''
    < 다른 풀이 >
    # 연속된 숫자가 나오지 않게 처리
    # 원소를 직접 리스트에 넣어 비교
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a
'''