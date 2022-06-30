# 코딩테스트 연습 / 해시 / 완주하지 못한 선수

def solution(participant, completion):    
    answer = ''
    participant.sort()
    completion.sort()
    
    for idx in range(len(participant)-1):
        if participant[idx] != completion[idx]:
            answer = participant[idx]
            break
    
    if answer == '':
        answer = participant[-1]
    
    return answer

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))


'''
import collections

def solution(participant, completion):
    print(collections.Counter(participant)) # Counter({'leo': 1, 'kiki': 1, 'eden': 1})
    print(collections.Counter(completion))  # Counter({'eden': 1, 'kiki': 1})
    print(answer)                           # Counter({'leo': 1})
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
'''