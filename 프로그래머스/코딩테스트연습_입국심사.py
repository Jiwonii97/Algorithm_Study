# https://school.programmers.co.kr/learn/courses/30/lessons/43238
'''
    문제를 확인해봤을 때, 1억, 10억과 같이 매우 큰 숫자를 다뤄야 하는 경우, 단순 BFS/DFS로 접근하면 시간초과가 날 것이다.
    그런 경우에는 이분탐색이 더 효율적일 것이다. 10억개를 모두 찾을 수 없기 때문이다
    이분탐색은 보통 특정 해를 하나로 가정하고 조건에 맞는지 하나씩 탐색해 나가며 1개가 남을때 까지 한다고 생각하면 된다
'''


def solution(n, times):
    left, right = 0, max(times)*n

    while left <= right:
        if left == right:
            break

        mid = left+(right-left)/2      # 오버플로 방지

        new_people = sum([mid//time for time in times])
        if new_people > n:
            right = mid-1
        elif new_people == n:
            right = mid
        else:       # new_prople < n
            left = mid+1

    return int(left)


print(solution(6, [7, 10]))
print(solution(6, [10, 1]))     # 6
print(solution(6, [2, 5]))      # 10
