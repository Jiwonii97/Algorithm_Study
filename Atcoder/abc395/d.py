import sys

n, q = map(int, sys.stdin.readline().strip().split())

nest = {i: [i] for i in range(1, n+1)}     # 둥지 현황
pigeon = {i: i for i in range(1, n+1)}        # 비둘기 위치

for _ in range(q):
    tasks = list(map(int, sys.stdin.readline().strip().split()))

    if tasks[0] == 1:
        pg, end = tasks[1:]
        start = pigeon[pg]
        pigeon[pg] = end

        nest[end].append(pg)   # 시작점의 비둘기를 옮기고
        nest[start].remove(pg)      # 그곳의 비둘기 제거

    elif tasks[0] == 2:
        start, end = tasks[1:]

        # 비둘기 위치 현황 수정
        for n in nest[start]:
            pigeon[n] = end
        for n in nest[end]:
            pigeon[n] = start

        # 둥지 스왑
        nest[end], nest[start] = nest[start], nest[end]

    elif tasks[0] == 3:
        print(pigeon[tasks[1]])
