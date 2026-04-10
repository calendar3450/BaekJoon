from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    q = deque([1])
    dist = [-1] * (n+1)
    dist[1] = 0
        
    while q:
        cur = q.popleft()
        for nx in graph[cur]:
            if dist[nx] == -1:
                dist[nx] = dist[cur] +1
                q.append(nx)
                
    max_dist = max(dist[1:])
    answer = dist.count(max_dist)
    return answer