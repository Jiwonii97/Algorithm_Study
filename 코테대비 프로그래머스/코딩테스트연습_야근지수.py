import heapq


def solution(n, works):
    max_heap = []
    for item in works:
        heapq.heappush(max_heap, (-item, item))

    for _ in range(n):
        nw = heapq.heappop(max_heap)[1]
        inputData = max(0, nw-1)
        heapq.heappush(max_heap, (-inputData, inputData))

    return sum([x[1]**2 for x in max_heap])


print(solution(4, [4, 3, 3]))
print(solution(1, [2, 1, 2]))
print(solution(3, [1, 1]))
