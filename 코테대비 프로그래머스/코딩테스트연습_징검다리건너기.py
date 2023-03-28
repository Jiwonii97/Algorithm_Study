# https://school.programmers.co.kr/learn/courses/30/lessons/64062

def solution(stones, k):
    left, right = 1, 200000000

    while left <= right:
        mid = (left+right)//2

        steps = 0
        for stone in stones:
            if stone <= mid:
                steps += 1
            else:
                steps = 0

            if steps >= k:
                break

        if steps >= k:
            right = mid-1
        else:
            left = mid + 1

    return left


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
