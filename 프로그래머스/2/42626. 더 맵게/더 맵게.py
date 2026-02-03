import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    n = len(scoville)
    
    for i in scoville:
        heapq.heappush(heap,i)
    
    while  heap[0] <K and len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        mixed = a+(b*2)
        
        heapq.heappush(heap,mixed)
        answer +=1
        
    if len(heap) == 1 and heap[0] <K:
        return -1
    
    return answer