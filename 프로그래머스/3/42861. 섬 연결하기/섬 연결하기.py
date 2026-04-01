def solution(n, costs):
    costs.sort(key = lambda x: x[2])
    parents = [i for i in range(n)]
    
    def press(x):
        while parents[x] != x:
            parents[x] = parents[parents[x]]
            x = parents[x]
        return x
    
    def union (a,b):
        a,b = press(a),press(b)
        if a== b:
            return False
        parents[a] = b
        return True
    
    total = 0
    for a, b, cost in costs:
        if union(a, b):  # 사이클 아니면 선택
            total += cost
    
    return total
