# 코딩테스트 연습 / Summer/Winter Coding(~2018) / 점프와 순간 이동
# 2로 계속 나누며 나눠 지지 않는 경우 앞으로 한칸을 이동하는 방식 사용

def solution(n):
    ans = 0
    while n > 0:
        n, m = divmod(n, 2)
        if m == 1:
            ans += 1

    return ans

print(solution(5))          # 2
print(solution(6))          # 2
print(solution(5000))          # 5


'''
    < 다른 풀이 >
    # 직접 이진수로 바꿔서 1의 개수(나머지)만 파악하는 방식
    def solution(n):
        return bin(n).count('1')
'''