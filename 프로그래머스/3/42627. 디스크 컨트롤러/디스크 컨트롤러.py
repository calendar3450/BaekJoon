import heapq

def solution(jobs):
    jobs = sorted(jobs)
    
    waiting = []
    time = 0
    index = 0
    total = 0
    
    while index < len(jobs) or waiting:
        while index < len(jobs) and jobs[index][0] <= time:
            request = jobs[index][0]
            duration = jobs[index][1]

            heapq.heappush(waiting, [duration, request])
            index += 1
            
        if waiting:
            duration, request = heapq.heappop(waiting)

            time += duration
            total += time - request
        else:
            time = jobs[index][0]
            
    return total // len(jobs)