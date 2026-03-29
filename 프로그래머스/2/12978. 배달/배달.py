import heapq

def solution(N, road, K):
    # dfs로 푼 방식 시간 초과.
#     answer = []
#     check = [False]*(N+1)
    
#     def DFS(start,cur_dis):
#         nonlocal answer,check
        
#         answer.append(start)
        
#         for r in road:
#             if start in r[0:2]:
#                 if start == r[0] and cur_dis+r[2]<=K and not check[r[1]]:
#                     check[r[1]] = True
#                     DFS(r[1],cur_dis+r[2])
#                     check[r[1]] = False
#                 elif start == r[1] and cur_dis+r[2]<=K:
#                     check[r[1]] = True
#                     DFS(r[0],cur_dis+r[2])
#                     check[r[1]] = False
#         return
    
#     check[1] = True 
#     DFS(1,0)
    
#     return len(list(set(answer)))

    graph = [[] for _ in range(N+1)]
    for a,b,c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))
        
    dist = [float('inf')] * (N+1)
    dist[1] = 0
    # 거리 시간 도로 순
    heap =[(0,1)]
    
    while heap:
        d,node = heapq.heappop(heap)
        if d > dist[node]:
            continue
        
        for nxt,cost in graph[node]:
            nd = d + cost
            if nd < dist[nxt]:
                dist[nxt] = nd
                heapq.heappush(heap,(nd,nxt))
    
    print(dist)
    
    return sum(1 for d in dist if d<= K)
    
    