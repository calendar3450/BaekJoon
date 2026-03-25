from collections import deque

def solution(land):
    row ,col = len(land), len(land[0])
    visited = [[False] * col for _ in range(row)]
    result = [0] * col
    queue = deque()
    
    for i in range(row):
        for j in range(col):
            if land[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                cnt =0
                queue.append((j,i))
                cols = set()
                
                while queue:
                    x,y = queue.popleft()
                    cnt +=1
                    cols.add(x)
                    
                    for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                        nx = x+dx
                        ny = y+dy
                        
                        if 0<=nx<col and 0<=ny<row and not visited[ny][nx] and land[ny][nx] ==1:
                            queue.append((nx,ny))
                            visited[ny][nx] = True
                for c in cols:
                    result[c] +=cnt
                    
    return max(result)