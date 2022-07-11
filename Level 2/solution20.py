# 코딩테스트 연습 / 연습문제 / 124 나라의 숫자
# 3진법 변환 문제와 유사
# 문제 풀이 방식을 확인

def solution(n):
    task = {"0":"4", "1":"1","2":"2"}
    answer = ""
    
    while n:
        answer += task[str(n%3)]
        n = n//3 if n%3 else n//3-1
    
    return answer[::-1]

print(solution(1))
print(solution(4))
print(solution(6))
print(solution(9))
print(solution(10))

'''
    < 다른 풀이 >
    # divmod 활용, 문자열에 직접적인 인덱스 활용
    def change124(n):
        if n<=3:
            return '124'[n-1]
        else:
            q, r = divmod(n-1, 3) 
            return change124(q) + '124'[r]
'''