from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque(priorities)
    queue_order = deque([i for i in range(len(priorities))])
    list_order =[]
    list_order_num =[]
    
    while queue:
        first = max(queue)
        check = queue.popleft()
        check_num = queue_order.popleft()
        
        if check == first:
            list_order.append(check)
            list_order_num.append(check_num)
        else:
            queue.append(check)
            queue_order.append(check_num)
            
        
    print(list_order)
    print(list_order_num)
        
    return list_order_num.index(location)+1