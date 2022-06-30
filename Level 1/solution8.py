# 코딩테스트 연습 / 월간 코드 챌린지 시즌3 / 없는 숫자 더하기
# 단순 수학 연산 (sum() 활용)

def solution(numbers):
    _list = list(range(10))
    
    for num in numbers:
        _list.remove(num)
    
    return sum(_list)


print(solution([1,2,3,4,6,7,8,0]))
print(solution([5,8,4,0,6,7,9]))

'''
< 다른 풀이 >
def solution(numbers):
    return 45 - sum(numbers)
'''