# https://school.programmers.co.kr/learn/courses/30/lessons/12987
'''
    투 포인트 구현 문제
    - 2개의 큰 분류 안에서 세부를 분류해 나가는 경우 사용
    - 한쪽의 포인트는 계속 증가 시키면서 나머지 하나는 조건에 만족하는 경우에만 움직임
    - 반복문을 하나만 사용하므로 시간 소모가 적음
'''


def solution(A, B):
    answer = 0

    # 두 리스트 오름차순 정렬
    A.sort()
    B.sort()
    idx = 0

    # 리스트 길이만큼 반복
    for a in range(len(A)):
        # B의 원소가 더 크면 answer와 idx + 1
        if A[idx] < B[a]:
            answer += 1
            idx += 1

    return answer


print(solution([5, 1, 3, 7], [2, 2, 6, 8]))
print(solution([2, 2, 2, 2], [1, 1, 1, 1]))


'''
    # 초기 아이디어
    # bisect를 통해 이진 탐색으로 위치를 찾고 정보를 얻자
    def solution(A, B):
        import bisect
        answer = 0

        B.sort()
        for a in A:
            idx = bisect.bisect_left(B, a)
            if idx == len(B):     # A팀의 숫자보다 높은 수가 없는 경우
                B.pop(0)
            elif a == B[idx]:     # 무승부인 경우
                del B[idx]
            else:           # B팀이 높은 숫자가 있는 경우
                del B[idx]
                answer += 1
        return answer
'''
