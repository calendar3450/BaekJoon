import sys
sys.setrecursionlimit(1000000)
from collections import deque

n,m = map(int,input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dist = [[-1] * m for _ in range(n)]

dirs = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

queue = deque()

for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            dist[i][j] =0
            queue.append((i,j))

while queue:
    x,y = queue.popleft()

    for dx,dy in dirs:
        cx,cy = x+dx , y+dy
        if 0<=cx<n and 0<=cy<m and dist[cx][cy] == -1:
            dist[cx][cy] = dist[x][y] +1
            queue.append((cx,cy))

ans = max(map(max,dist))
print(ans)