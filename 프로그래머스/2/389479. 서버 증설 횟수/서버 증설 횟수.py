from collections import deque
def solution(players, m, k):
    answer = 0
    queue = deque()
    total_server = len(queue)
    tick = 0

    
    for player in players:
        tick +=1
        
        if not(player < m*total_server + m):
            for i in range((player // m) - total_server):
                queue.append(tick+k-1)
                answer +=1
        while queue and queue[0] == tick:
            queue.popleft()
        
        total_server = len(queue)
        
    return answer