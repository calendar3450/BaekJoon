def solution(n, computers):
    answer = 0
    nodes = [False for _ in range(len(computers))]
    
    def DFS(cur_pos):
        if nodes[cur_pos]:
            return
        
        nodes[cur_pos] = True
        
        for i in range(len(computers)):
            if computers[cur_pos][i] == 1:
                DFS(i)
        
    for i in range(len(computers)):
        if not nodes[i]:
            DFS(i)
            answer+=1
            
    return answer