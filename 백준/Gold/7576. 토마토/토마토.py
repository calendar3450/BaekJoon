from collections import deque
cols, rows = map(int, input().split())
# cols,rows = 6,4
ans = 0
fresh = 0

# grid = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,1]]
grid = []
for _ in range(rows):
    line = list(map(int, input().split()))
    grid.append(line)

queue = deque()

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 1:
            queue.append((i,j))
        elif grid[i][j] == 0:
            fresh += 1

while queue:
    for _ in range(len(queue)):
        x,y = queue.popleft()
        for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
            nx,ny = x+dx,y+dy
            if 0<=nx<rows and 0<=ny<cols and grid[nx][ny] == 0:
                grid[nx][ny] = 1
                queue.append((nx,ny))
                fresh -= 1
    ans +=1

if fresh == 0:
    print(ans-1)
else:
    print(-1)
            