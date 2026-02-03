import heapq

def solution(n, works):
    answer = 0
    leng = len(works)
    heap = [-i for i in works]
    heapq.heapify(heap)
    
    
    if sum(works) <= n:
        return 0
    
    if sum(works) - n ==1:
        return 1
    
    if leng ==1:
        return (works[0]-n)**2
    
    for _ in range(n):
        o = -heapq.heappop(heap)
        if o ==0:
            break
        o-=1
        heapq.heappush(heap,-o)
    
    for i in heap:
        answer += (i**2)

    return answer