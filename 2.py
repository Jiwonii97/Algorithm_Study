# 코딩테스트 연습 / 2022 KAKAO BLIND RECRUITMENT / 신고 결과 받기
# 문자열 다루기 (list comprehension, index)

def solution(id_list, report, k):
    
    # reports = {x : 0 for x in id_list}
    _dict = {}
    for id in id_list:
        _dict[id] = 0
    
    ban = [name.split(' ')[1] for name in set(report)]
    ban_list = [name.split() for name in set(report)]
    ban_name = []
    
    for get in id_list:
        if ban.count(get) >= k:
            ban_name.append(get)
        
    for m1 in ban_list:
        if m1[1] in ban_name:
            _dict[m1[0]] += 1
    
    return list(_dict.values())

solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)
solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3)

'''
def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer
'''