# 코딩테스트 연습 / 탐욕법(Greedy) / 큰 수 만들기
# 스택을 활용한 그리디 문제
# 큰수를 만들기 위해서는 높은 자리수가 높아야 한다. 이를 이용하기 위해 Stack을 활용해 큰수가 들어 갈 수 있도록 조절한다

def solution(number, k):
    answer = [] # Stack
    
    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
        
    return ''.join(answer[:len(answer) - k])

print(solution("1924",2))
print(solution("1231234",3))
print(solution("4177252841",4))
print(solution("1234567",3))
print(solution("987654321",3))