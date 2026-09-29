import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    
    answer = 0
    heap = []
    for i in works:
        heapq.heappush(heap,-i)
    
    for i in range(n):
        work = -heapq.heappop(heap) -1
        heapq.heappush(heap,-work)
    
    return sum(work**2 for work in heap)