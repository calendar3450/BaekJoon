from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    result = []
    n = len(progresses)
    
    for i in range(n):
        result.append(math.ceil((100-progresses[i])/speeds[i]))
        
    resultd = deque(result)
    m = len(result)
    
    while resultd:
        start = resultd.popleft()
        ans = 1
        
        while resultd and start >= resultd[0]:
            resultd.popleft()
            ans+=1
        answer.append(ans)
    return answer