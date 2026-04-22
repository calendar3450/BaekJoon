from collections import deque

def solution(board):
    row = len(board)
    col = len(board[0])
    
    for i in range(row):
        for j in range(col):
            if board[i][j] == 'R':
                rx = j
                ry =i
            if board[i][j] == 'G':
                gx = j
                gy = i
                
    if 0 <gx< col-1 and 0 <gy < row-1 and board[gy][gx+1] == '.' and board[gy][gx-1] == '.' and board[gy+1][gx] == '.' and board[gy-1][gx] == '.':
        return -1
    
    visited = [[False]*col for _ in range(row)]
    visited[ry][rx] = True
    queue = deque([(rx,ry,0)])
    
    while queue:
        x,y,cnt = queue.popleft()
        
        if board[y][x] == 'G':
            return cnt
        
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            ny,nx = y,x
            
            while 0<= ny+dy < row and 0<= nx+dx < col and board[ny+dy][nx+dx] != 'D':
                ny += dy
                nx += dx
                
            if not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((nx,ny,cnt+1))
        
    return -1