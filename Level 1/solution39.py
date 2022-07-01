# 코딩테스트 연습 / 연습문제 / 문자열을 정수로 바꾸기
# 문자열에 -가 있어도 정수로 변환시켜줌

def solution(s):
    return int(s) if s[0] != "-" else -int(s[1:])

    # return int(s)