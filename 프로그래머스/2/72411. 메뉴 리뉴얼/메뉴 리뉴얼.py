def solution(orders, course):
    result = []
    candidate = {}
    order = orders[0]
    
    def backtracking(cur,cour,order,procedure):
        nonlocal candidate
        
        if len(cur) == cour:
            cur = "".join(sorted(cur))
            if cur not in candidate:
                candidate[cur] = 1
            else:
                candidate[cur] +=1
            return
        
        for i in range(procedure,len(order)):
            cur+=order[i]
            backtracking(cur,cour,order,i+1)
            cur = cur[:-1]
    
    for order in orders:
        for cour in course:
            backtracking("",cour,order,0)
    
    
    for cour in course:
        maximum = 0
        for i in candidate:
            if len(i) == cour:
                if maximum <= candidate[i]:
                    maximum = candidate[i]
                    
        if maximum <2:
            continue
        
        for i in candidate:
             if len(i) == cour and maximum == candidate[i]:
                    result.append(i)

    return sorted(result)