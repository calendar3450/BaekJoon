import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
check = [[0]*m for _ in range(n)]
ans_cnt = 0
ans_area = 0

def DFS(x, y):
    if x < 0 or x >= n or y < 0 or y >= m: 
        return 0
    if check[x][y] == 1 or matrix[x][y] == 0:
        return 0

    check[x][y] = 1
    
    area = 1
    area += DFS(x + 1, y)
    area += DFS(x - 1, y)
    area += DFS(x, y + 1)
    area += DFS(x, y - 1)
    
    return area

for x in range(n):
    for y in range(m):  
        if matrix[x][y] == 1 and check[x][y] == 0:
            ans_cnt += 1
            current_area = DFS(x, y)
            ans_area = max(ans_area, current_area)

print(ans_cnt)
print(ans_area)

