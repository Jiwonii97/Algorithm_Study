# 코딩테스트 연습 / 깊이/너비 우선 탐색(DFS/BFS) / 여행경로
answer = []


def dfs(curCity, leftTickets, curRoad):
    global answer
    if not leftTickets:
        answer.append(curRoad)
        return

    for ticket in leftTickets:
        dep, arr = ticket
        if dep == curCity:
            nextTicket = leftTickets.copy()
            nextTicket.remove(ticket)
            dfs(arr, nextTicket, curRoad+[arr])


def solution(tickets):
    global answer
    answer = []
    dfs("ICN", tickets, ["ICN"])

    print(answer)
    return sorted(answer)[0]


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], [
    "SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
