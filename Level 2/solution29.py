# 코딩테스트 연습 / 탐욕법(Greedy) / 조이스틱
# 시작은 무조건 1번째 단어에서 출발
# 그리디 알고리즘 활용하여 코드 진행하며 최소값을 계속 갱신하는 문제
    
def solution(name):
    answer = 0
    words = [min(ord(x)-ord('A'), ord('Z')-ord(x)+1) for x in name]
    
    slen = len(name)-1    # 좌우 이동거리
    next_idx = 0    # A의 개수를 확인해 줄 인덱스
    
    # 진행 하는 중간중간 0을 만나면 왔던길을 다시가는 것과 이어서 가는 것 중 최적값을 탐색
    for idx, word in enumerate(words):
        answer += word  # 현재 이동값을 더하고
        next_idx = idx + 1      # 다음 인덱스에서 확인
        
        # 연속된 A를 탐색
        while next_idx < len(name) and words[next_idx] == 0:
            next_idx += 1
        
        # 시작지점에서 (1) 정상적으로 가는것, (2) 왼쪽으로 갔다가 다시오는 것, (3) 오른쪽으로 갖다가 다시오는 것
        # 최소값을 찾아 이동하면 이동을 적게 할 수 있음
        slen = min(slen,idx*2+(len(name)-next_idx),idx + 2*(len(name)-next_idx))
        
    return answer + slen

print(solution("JEROEN"))
print(solution("JAN"))
print(solution("JAZ"))
print(solution("JAACAZ"))