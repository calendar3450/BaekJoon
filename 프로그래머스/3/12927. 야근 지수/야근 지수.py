import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    
    answer = 0
    heap = []
    for i in works:
        heapq.heappush(heap,-i)
        
    for i in range(n):
        work = heapq.heappop(heap) * -1
        work -=1
        heapq.heappush(heap,-work)
        
    for i in heap:
        answer += (i**2)
    
    return answer