# 코딩테스트 연습 / 힙(Heap) / 이중우선순위큐

def solution(operations):
    import heapq
    hq = []
    
    for task in operations:
        # 빈 배열인 경우에 데이터를 제거하려고 하면 패스함
        if task[0] == "D" and not hq:
            continue
        
        # 작업 진행
        if task == "D -1":
            heapq.heappop(hq)
        elif task == "D 1":
            hq = sorted(hq)[:-1]
        else:
            num = int(task.split()[1])
            heapq.heappush(hq,num)
    
    return [max(hq), min(hq)] if hq else [0,0]

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
print(solution(["I 6", "I 2", "I 1", "I 4", "I 5", "I 3", "D 1", "I 7", "D -1", "I 6", "D -1", "D -1"]))
print(solution(["I 3", "I 2", "I 1", "D 1", "D 1", "I 3", "D -1"]))
print(solution(["I 2","I 4","D -1", "I 1", "D 1"]))