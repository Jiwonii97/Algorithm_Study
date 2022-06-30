# 코딩테스트 연습 / 2019 KAKAO BLIND RECRUITMENT / 실패율

# ★★★★★★★★★★★★★★★★★★★★★★
# sorted -> dictionary를 넣으면 sort된 list를 반환해줌
# result는 dictionary이므로 sorted에 result를 그냥 넘기면 result의 keys가 들어갑니다.
# keys는 생략이 가능합니다. 거기에 lambda는 기준을 result[x]: 즉 value로 정렬한다는 뜻입니다. 그래서 key가 출력

def solution(N, stages):
    result = {}
    length = len(stages)
    stages.sort()
    print(stages)
    for stage in range(1, N+1):
        if length != 0:
            count = stages.count(stage)
            result[stage] = count / length
            length -= count
        else:
            result[stage] = 0
            
    return sorted(result, key=lambda x : result[x], reverse=True)

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4,[4,4,4,4,4]))

'''
< 다른 풀이 >
def solution(N, stages):
    answer = []
    fail = []
    info = [0] * (N + 2)
    for stage in stages:
        info[stage] += 1
    for i in range(N):
        be = sum(info[(i + 1):])
        yet = info[i + 1]
        if be == 0:
            fail.append((str(i + 1), 0))
        else:
            fail.append((str(i + 1), yet / be))
    for item in sorted(fail, key=lambda x: x[1], reverse=True):
        answer.append(int(item[0]))
    return answer
'''