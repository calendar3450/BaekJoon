from collections import deque

def solution(board):
    row = len(board)
    col = len(board[0])
    
    
    for i in range(row):
        for j in range(col):
            if board[i][j] == 'G':
                gy, gx = i,j
            if board[i][j] == 'R':
                ry , rx = i,j
    
    if 0 <gx< col-1 and 0 <gy < row-1 and board[gy][gx+1] == '.' and board[gy][gx-1] == '.' and board[gy+1][gx] == '.' and board[gy-1][gx] == '.':
        return -1
    
    visited = [[False] * col for _ in range(row)]
    visited[ry][rx] = True
    q = deque([(ry, rx, 0)])
    
    while q:
        y, x, cnt = q.popleft()
        
        if board[y][x] == 'G':
            return cnt
        
        for dy,dx in [(0,1),(0,-1),(1,0),(-1,0)]:
            ny,nx = y,x
            
            while 0<= ny+dy < row and 0<= nx+dx < col and board[ny+dy][nx+dx] != 'D':
                ny += dy
                nx += dx
                
            # 멈춘 위치가 미방문이면 큐에 추가
            if not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx, cnt+1))
                
    return -1


# from collections import deque
# def solution(board):
#     row = len(board)
#     col = len(board[0])
    
#     for i in range(row):
#         for j in range(col):
#             if board[i][j] == 'R':
#                 sy, sx = i, j
    
#     visited = [[False] * col for _ in range(row)]
#     visited[sy][sx] = True
#     q = deque([(sy, sx, 0)])
    
#     while q:
#         y, x, cnt = q.popleft()
        
#         if board[y][x] == 'G':
#             return cnt
        
#         for dy, dx in [(0,1),(0,-1),(1,0),(-1,0)]:
#             ny, nx = y, x
#             while 0<=ny+dy<row and 0<=nx+dx<col and board[ny+dy][nx+dx] != 'D':
#                 ny += dy
#                 nx += dx
            
#             if not visited[ny][nx]:
#                 visited[ny][nx] = True
#                 q.append((ny, nx, cnt+1))
    
#     return -1