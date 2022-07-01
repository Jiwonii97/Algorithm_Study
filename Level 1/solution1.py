# 코딩테스트 연습 / 연습문제 / 약수의 합

def solution(n):
    answer = []
    for idx in range(1,n+1):
        if n%idx == 0:
            answer.append(int(n/idx))
            answer.append(idx)
            
    return sum(set(answer))

'''
    # 나누어지는 약수만 찾아 sum으로 더함
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])
    return sum([i for i in range(1,num+1) if num%i==0])
'''