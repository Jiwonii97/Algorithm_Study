# 코딩테스트 연습 / 월간 코드 챌린지 시즌1 / 3진법 뒤집기
# 정수의 진수 변환을 보여주는 좋은 예

def solution(n):
    answer = ''
    
    while(True):
        n, b = divmod(n,3)
        answer += str(b)
        if n == 0:
            break
            
    return int(answer,3)