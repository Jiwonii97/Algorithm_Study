# 코딩테스트 연습 / 연습문제 / 이상한 문자 만들기
# upper, lower 활용

def solution(s):
    answer = ""
    for text in s.split(" "):
        for idx in range(len(text)):
            if (idx+1)%2 != 0:
                answer += text[idx].upper()
            else:
                answer += text[idx].lower()
        answer += " "
    return answer[:-1]