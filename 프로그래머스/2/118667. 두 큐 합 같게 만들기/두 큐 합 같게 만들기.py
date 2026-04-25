from collections import deque

def solution(queue1, queue2):
    answer = 0
    n = len(queue1)
    q1 = deque(queue1)
    q2 = deque(queue2)
    q1_sum = sum(q1)
    q2_sum = sum(q2)
    
    for _ in range(n*10):
        if q1_sum == q2_sum:
            return answer
        
        if q1_sum < q2_sum:
            tmp = q2.popleft()
            q2_sum -= tmp
            q1.append(tmp)
            q1_sum += tmp
            answer +=1
        
        elif q1_sum > q2_sum:
            tmp = q1.popleft()
            q1_sum -= tmp
            q2.append(tmp)
            q2_sum += tmp
            answer+=1
        
    return -1