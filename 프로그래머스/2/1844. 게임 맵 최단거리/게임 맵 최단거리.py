from collections import deque
def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    
    queue = deque()
    dist = [[0]*m for _ in range(n)]
    queue.append((0,0))
    dist[0][0] = 1
    
    posX = [1,-1,0,0]
    posY = [0,0,1,-1]
    
    while queue:
        x,y = queue.popleft()
        
        if x == m-1 and y == n-1:
            return dist[y][x]
        
        for i in range(4):
            nx = x+posX[i]
            ny = y+posY[i]
            
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
                
            if maps[ny][nx] == 0 or dist[ny][nx] != 0:
                continue
                
            queue.append((nx,ny))
            dist[ny][nx] = dist[y][x]+1
    
    return -1
