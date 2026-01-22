from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    cur_bridge = deque([0]*bridge_length)
    wait = deque(truck_weights)
    cur_weight = 0
    
    while wait or cur_weight > 0:
        answer += 1
        
        out = cur_bridge.popleft()
        cur_weight-=out
        
        if wait and cur_weight + wait[0] <=weight:
            cur_car = wait.popleft()
            cur_bridge.append(cur_car)
            cur_weight += cur_car
        else:
            cur_bridge.append(0)

    return answer