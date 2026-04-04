from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    result = 0
    
    def BFS(x,y,target):
        q = deque([(x,y,0)])
        check=[[False]*m for _ in range(n)]
        check[y][x] = True
        
        while q:
            x,y,sec = q.popleft()
            
            if maps[y][x] == target:
                return sec
            
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx = x + dx
                ny = y + dy
                if 0<=nx<m and 0<=ny<n and not check[ny][nx] and maps[ny][nx] != 'X':
                    q.append((nx,ny,sec+1))
                    check[ny][nx] = True
        return -1
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                sx, sy = j, i
            elif maps[i][j] == 'L':
                lx, ly = j, i
                
    s_to_l = BFS(sx, sy, 'L')
    l_to_e = BFS(lx, ly, 'E')       
    
    if s_to_l == -1 or l_to_e == -1:
        return -1
    return s_to_l + l_to_e
        