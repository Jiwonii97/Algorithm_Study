# 코딩테스트 연습 / 2021 KAKAO BLIND RECRUITMENT / 신규 아이디 추천
# 정규식 문제

def solution(new_id):
    answer = ''
    tsmj = list("~!@#$%^&*()=+[{]}:?,<>/")
    
    for idx in range(len(new_id)):
        if new_id[idx] in tsmj:
            continue
        else:
            answer += new_id[idx].lower()
    
    while(True):
        answer = answer.replace('..','.')
        if answer.find("..") == -1:
            break

    # 첫글자, 마지막 . 제거
    if answer[0] == '.':
        answer = answer[1:]
    elif answer[-1] == '.':
        answer = answer[:-1]
        
    # new_id가 빈 문자열이라면, new_id에 "a"를 대입
    if answer == '':
        answer += 'a'
    
    # new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복
    while(len(answer) <= 2):
        tmp = answer[-1]
        answer += tmp
        
    # 글자수 15자 제한
    if len(answer) > 15:
        answer = answer[:15]
    
    # 첫글자, 마지막 . 제거
    if answer[0] == '.':
        answer = answer[1:]
    elif answer[-1] == '.':
        answer = answer[:-1]
    
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))

'''
< 다른 풀이 > - 정규식!!
import re
def solution(new_id):    
    #1단계 & 2단계 소문자 치환, 제거
    answer = re.sub('[^0-9a-z_.\-]+','',new_id.lower())
    
    #3단계 . 2번 이상을 1개로 압축
    answer = re.sub('\.\.+','.',answer)
    
    #4단계 양끝 . 제거
    answer = answer.strip('.')
    
    #5단계 빈문자열 a 추가
    if answer =='': answer='a'
        
    #6단계 15개제외하고 문자모두제거, 우측 . 제거
    answer = answer[:15].rstrip('.')
        
    #7단계 길이 3 될 때까지 끝 문자 추가    
    answer+=answer[-1]*(3-len(answer))
        
    return answer
'''