# 코딩테스트 연습 / 2018 KAKAO BLIND RECRUITMENT / [1차] 뉴스 클러스터링
from math import floor
def solution(str1, str2):
    answer = 0
    str1, str2 = str1.lower(), str2.lower()
    arr1 = []
    arr2 = []
    
    # 문자열 분리
    for idx in range(len(str1)-1):
        s = str1[idx:idx+2]
        if s.isalpha(): arr1.append(s)
            
    for idx in range(len(str2)-1):
        s = str2[idx:idx+2]
        if s.isalpha(): arr2.append(s)
    
    # 교집합, 합집합
    res1 = set(arr1).union(set(arr2))
    res2 = set(arr1).intersection(set(arr2))
    
    if len(res1) == 0: return 65536
    
    union_len = sum([max(arr1.count(union), arr2.count(union)) for union in res1])
    intersection_len = sum([min(arr1.count(intersection), arr2.count(intersection)) for intersection in res2])
    
    answer = floor(65536*(intersection_len/union_len))
    
    return answer

print(solution("FRANCE","french"))	# 16384
print(solution("handshake","shake hands"))	# 65536
print(solution("aa1+aa2","AAAA12"))	# 43690
print(solution("E=M*C^2","e=m*c^2"))   # 65536
print(solution("A+C","DEF"))        # 65536