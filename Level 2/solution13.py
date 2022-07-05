# 코딩테스트 연습 / 해시 / 베스트앨범

def solution(genres, plays):
    answer = []
    songs = {}
    
    for idx, song in enumerate(genres):
        # 있으면
        if song in songs.keys():
            songs[song][0].append([idx, plays[idx]])
            songs[song][1] += plays[idx]
        # 없으면
        else :
            songs[song] = [[[idx, plays[idx]]],plays[idx]]
            
    # 우선 카테고리별 정렬
    for cg in songs.keys():
        songs[cg][0].sort(key = lambda x : x[1], reverse = True)
    temp = sorted(songs.values(), key = lambda x : x[1], reverse = True)
    
    for tmp in temp:
        answer += [x[0] for x in tmp[0]][:2]

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))

'''
    < 다른 풀이 >
    def solution(genres, plays):
        answer = []
    d = {e:[] for e in set(genres)} # 딕셔너리에 미리 항목 추가
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])   # 데이터 넣기
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x]) ), reverse = True)
    # d[x]에 해당하는 y[0]를 모두 더해서 그걸 기준으로 역순의 정렬 리스트를 리턴시킴
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer
'''