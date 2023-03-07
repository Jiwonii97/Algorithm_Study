# https://school.programmers.co.kr/learn/courses/30/lessons/136798

'''
    약수의 개수 찾기
'''


def solution(number, limit, power):
    answer = 0

    ys = []

    for num in range(1, number+1):
        cnt = 0
        for i in range(1, int(num**0.5)+1):
            if i*i == num:
                cnt += 1
            elif num % i == 0:
                cnt += 2
        ys.append(cnt)

    for attack in ys:
        if attack <= limit:
            answer += attack
        else:
            answer += power

    return answer

    # return sum([power if i > limit else i for i in arr])


print(solution(5, 3, 2))
print(solution(10, 3, 2))
