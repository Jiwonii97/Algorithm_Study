# 코딩테스트 연습 / 2018 KAKAO BLIND RECRUITMENT / [1차] 캐시
# queue 형태를 사용하여 캐시를 관리하고 들어오는 데이터에 따라 우선순위를 수정하며 캐시를 업데이트 하였다

def solution(cacheSize, cities):
    answer = 0
    
    caches = []
    
    # 캐시 사이즈가 0인 경우, 모든 경우를 cache miss로 적용한다
    if cacheSize == 0:
        return len(cities)*5
    
    for city in cities:
        city = city.lower()
        # 해당 도시가 이미 캐시에 있는 경우, 우선순위를 늘림
        if city in caches:
            answer += 1     # cache hit
            caches.remove(city)
            caches.append(city)
        # 해당 도시는 없지만 캐시에 공간이 여유로우면
        elif len(caches) < cacheSize:
            answer += 5     # cache miss
            caches.append(city)
        # 도시도 없고, 캐시도 차있어 우선순위에 따라 pop(0) 진행후 새로운 데이터 업데이트
        else:
            answer += 5     # cache miss
            caches.pop(0)
            caches.append(city)
    
    return answer


# 출력
print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))     	# 50
print(solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))        	# 21
print(solution(2,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))        	# 60
print(solution(5,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))        	# 52
print(solution(2,["Jeju", "Pangyo", "NewYork", "newyork"]))     	# 16
print(solution(0,["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))     	# 25


'''
    < 다른 풀이 >
    # 풀이의 경우 collections의 deque와 maxlen을 사용하여 불필요한 과정을 생략하였다.(전체적인 개수 확인)
    def solution(cacheSize, cities):
        import collections
        cache = collections.deque(maxlen=cacheSize)
        time = 0
        for i in cities:
            s = i.lower()
            if s in cache:
                cache.remove(s)
                cache.append(s)
                time += 1
            else:
                cache.append(s)
                time += 5
        return time
'''