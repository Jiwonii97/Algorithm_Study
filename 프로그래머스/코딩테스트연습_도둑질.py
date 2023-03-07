# https://school.programmers.co.kr/learn/courses/30/lessons/42897

def solution(money):
    # 첫번째 집을 터는 경우
    dp1 = [money[0]]+[0]*(len(money)-1)
    for i in range(1, len(money)-1):
        dp1[i] = max(dp1[i-1], dp1[i-2]+money[i])

    # 첫번째 집을 털지 않는 경우
    dp2 = [0]*len(money)
    for i in range(1, len(money)):
        dp2[i] = max(dp2[i-1], dp2[i-2]+money[i])

    return max(dp1[-2], dp2[-1])


print(solution([1, 2, 3, 1]))
