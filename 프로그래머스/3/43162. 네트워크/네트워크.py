def solution(n, computers):
    answer = 0
    check = [False] * n
    
    def DFS(cur):
        if check[cur]:
            return
        
        check[cur] = True
        
        for i in range(n):
            if computers[cur][i] == 1:
                DFS(i)
                
    for i in range(n):
        if not check[i]:
            DFS(i)
            answer+=1
            
    return answer