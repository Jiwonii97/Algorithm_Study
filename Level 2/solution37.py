# 코딩테스트 연습 / 연습문제 / JadenCase 문자열 만들기

def solution(s):
    s=s.lower()
    answer = ""
    w1 = ""
    for ss in list(s):
        if w1 == "" or w1 == " ":
            answer += ss.upper()
        else:
            answer += ss
        w1 = ss
    return answer

print(solution("3people unFollowed me"))        # "3people Unfollowed Me"
print(solution("for the last week"))        # "For The Last Week"
print(solution("for the    last week"))        # "For The Last Week"

'''
    s.title() -> 문자열 내 띄어쓰기 기준으로 각 단어의 첫글자는 대문자로, 나머지는 소문자로 변환
    해당 문장에서는 공백이 연속으로 나올수 있어 split()을 진행 할 수 없으므로 사용은 안됨
'''