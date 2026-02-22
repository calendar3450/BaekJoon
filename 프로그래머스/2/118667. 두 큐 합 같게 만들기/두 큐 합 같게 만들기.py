from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1s = sum(queue1)
    q2s = sum(queue2)
    total = q1s + q2s
    
    # 전체가 홀수면 ㄴ답임.
    if total %2 != 0:
        return -1
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    # 같은경우
    if q1s == q2s:
        return 0
    
    for _ in range(len(queue1) * 3):
        if q1s == q2s:
            return answer
        
        # q1이 더 큰 경우
        if q1s > q2s:
            qp = queue1.popleft()
            q1s -=qp
            q2s += qp
            queue2.append(qp)
            answer+=1
        
        # q2가 더 큰 경우
        if q2s > q1s:
            qp = queue2.popleft()
            q2s -=qp
            q1s +=qp
            queue1.append(qp)
            answer+=1
            
    if q1s != q2s:
        return -1
    else:
        return answer
        