import heapq

def solution(operations):
    answer = []
    heap = []
    
    for operation in operations:
        d = operation.split(' ')
        if d[0] == 'I':
            heapq.heappush(heap,int(d[1]))
            
        elif d[0] == 'D':
            if heap:
                if d[1] =='-1':
                    heapq.heappop(heap)
                else:
                    heap.remove(max(heap))
                    
    if not heap:
        return [0,0]
    else:
        return [max(heap),min(heap)]
    
    return answer