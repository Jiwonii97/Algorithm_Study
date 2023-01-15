# 코딩테스트 연습 / 연습문제 / 숫자 블록
# 약수를 이용하는 문제, 약수 탐색은 제곱근까지 진행하면 된다는 걸 인지할 것

def solution(begin, end):
    answer = []

    for number in range(begin, end+1):
        if number == 1:
            answer.append(0)
            continue
        for i in range(2, int(number**0.5)+1):
            if number % i == 0 and number//i <= 10000000:
                answer.append(number//i)
                break
        else:
            answer.append(1)

    return answer


print(solution(1, 10))      # [0, 1, 1, 2, 1, 3, 1, 4, 3, 5]
print(solution(3, 6))
