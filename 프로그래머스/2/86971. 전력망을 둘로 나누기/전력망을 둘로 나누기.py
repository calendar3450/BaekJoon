from collections import deque
def solution(n, wires):
    answer = n
    graphs = [[] for _ in range(n+1)]
    
    for a,b in wires:
        graphs[a].append(b)
        graphs[b].append(a)
        
    for a,b in wires:
        visited = [False] * (n+1)
        queue = deque([1])
        visited[1] = True
        count = 1
        
        while queue:
            node = queue.popleft()
            
            for next_node in graphs[node]:
                if (node == a and next_node == b) or (node == b and next_node == a):
                    continue
                    
                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)
                    count += 1
                    
        answer = min(answer, abs(n - 2 * count))
        
    return answer