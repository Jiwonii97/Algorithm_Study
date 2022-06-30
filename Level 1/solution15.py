# 코딩테스트 연습 / 찾아라 프로그래밍 마에스터 / 폰켓몬

from math import floor
def solution(nums):
    answer = 0
    _list = []
    for num in nums:
        if num in _list:
            continue
        else:
            _list.append(num)
    
    size = floor(len(nums)/2)
    answer = min(size,len(_list))
    
    return answer

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))

'''
< 다른 풀이 >
# 중복을 제거하는 가장 쉬운 방법 : list를 set으로 변경
def solution(ls):
    return min(len(ls)/2, len(set(ls)))
'''