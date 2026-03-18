from collections import deque

def solution(maps):
    # m: 세로(행), n: 가로(열)
    m = len(maps)
    n = len(maps[0])
    
    # 상하좌우 이동을 위한 좌표 (nx를 행 변화량으로 사용)
    pos_x = [-1, 1, 0, 0] # 행(Row) 이동
    pos_y = [0, 0, -1, 1] # 열(Col) 이동
    
    queue = deque()
    queue.append((0, 0))
    
    dist = [[0] * n for _ in range(m)]
    dist[0][0] = 1
    
    while queue:
        x, y = queue.popleft() # x: 행, y: 열
        
        # 도착점 체크 (행은 m-1, 열은 n-1)
        if x == m - 1 and y == n - 1:
            return dist[x][y]
        
        for i in range(4):
            nx = x + pos_x[i]
            ny = y + pos_y[i]
            
            # 경계 체크 수정: nx는 m(행)과, ny는 n(열)과 비교
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            
            # 벽이거나 이미 방문한 경우
            if maps[nx][ny] == 0 or dist[nx][ny] != 0:
                continue
            
            queue.append((nx, ny))
            dist[nx][ny] = dist[x][y] + 1
            
    return -1