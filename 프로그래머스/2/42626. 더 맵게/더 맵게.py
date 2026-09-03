import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K and len(scoville)>=2:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        sum_ab = a + (b*2)
        
        heapq.heappush(scoville,sum_ab)
        answer +=1
    
    if len(scoville) == 1 and scoville[0] <K:
        return -1
    else:
        return answer