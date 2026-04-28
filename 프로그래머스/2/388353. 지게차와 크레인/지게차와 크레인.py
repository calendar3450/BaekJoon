from collections import deque

def solution(storage, requests):
    # 2차원 리스트로 변환 + 테두리 '0' 추가
    row = len(storage)
    col = len(storage[0])
    grid = [['0'] * (col + 2)]
    for s in storage:
        grid.append(['0'] + list(s) + ['0'])
    grid.append(['0'] * (col + 2))
    
    row += 2
    col += 2
    
    def mark_outside():
        # 외부와 연결된 빈 칸을 '0'으로 통일 (BFS)
        visited = [[False] * col for _ in range(row)]
        q = deque([(0, 0)])
        visited[0][0] = True
        
        while q:
            y, x = q.popleft()
            for dy, dx in [(0,1),(0,-1),(1,0),(-1,0)]:
                ny, nx = y+dy, x+dx
                if 0<=ny<row and 0<=nx<col and not visited[ny][nx]:
                    if grid[ny][nx] == '0' or grid[ny][nx] == '1':
                        grid[ny][nx] = '0'  # 외부와 연결된 빈 칸
                        visited[ny][nx] = True
                        q.append((ny, nx))
    
    for req in requests:
        target = req[0]
        
        if len(req) == 2:
            # 크레인: 해당 종류 전부 제거
            for i in range(row):
                for j in range(col):
                    if grid[i][j] == target:
                        grid[i][j] = '1'  # 내부 빈 칸 (아직 외부 연결 모름)
            mark_outside()
        
        else:
            # 지게차: 외부 접근 가능한 것만 제거
            mark_outside()
            to_remove = []
            for i in range(row):
                for j in range(col):
                    if grid[i][j] == target:
                        for dy, dx in [(0,1),(0,-1),(1,0),(-1,0)]:
                            ny, nx = i+dy, j+dx
                            if 0<=ny<row and 0<=nx<col and grid[ny][nx] == '0':
                                to_remove.append((i, j))
                                break
        
            for y, x in to_remove:
                grid[y][x] = '0'
                
    # 남은 컨테이너 수 세기
    count = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] not in ('0', '1'):
                count += 1
    
    return count