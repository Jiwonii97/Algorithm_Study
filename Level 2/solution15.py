# 코딩테스트 연습 / 힙(Heap) / 디스크 컨트롤러

def solution(jobs):
    import heapq
    
    jobs = [[x[1],x[0]] for x in jobs]
    cnt = length_ = len(jobs)
    stime, etime = -1, 0
    answer = 0
    hq = []
    heapq.heapify(hq)
    
    # jobs의 길이만큼 반복 진행
    while cnt:
        for job in jobs:
            if stime < job[1] <= etime:
                heapq.heappush(hq,job)
                
        # heap queue에 값이 있는 경우, 하나씩 가져와 계산
        if hq:
            jb = heapq.heappop(hq)
            stime = etime
            etime += jb[0]
            answer += (etime-jb[1])
            cnt -= 1
        else:
            etime += 1
    
    return int(answer/length_)

print(solution([[0, 3], [1, 9], [2, 6]]))

'''
    < Tip : OS 컨트롤러 - Shortest-Job-First(SJF) > 
    SJF는 가장 짧게 수행되는 프로세스가 가장 먼저 수행되는 것, FCFS에서 보았듯이 수행 시간이 짧은 프로세스가 먼저 오는 것이 평균 대기시간이 짧음

    디스트 컨트롤러 문제는 os 컨트롤러인 SJF를 물어보는 문제와 동일하다
    시작 시간과 수행시간을 볼때 각 태스크에서 수행시간이 적은 순서대로 작업을 진행하면 된다
    
    < 다른 풀이 >
    import heapq
    from collections import deque

    def solution(jobs):
        tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
        q = []
        heapq.heappush(q, tasks.popleft())
        current_time, total_response_time = 0, 0
        while len(q) > 0:
            dur, arr = heapq.heappop(q)
            current_time = max(current_time + dur, arr + dur)
            total_response_time += current_time - arr
            while len(tasks) > 0 and tasks[0][1] <= current_time:
                heapq.heappush(q, tasks.popleft())
            if len(tasks) > 0 and len(q) == 0:
                heapq.heappush(q, tasks.popleft())
        return total_response_time // len(jobs)
'''