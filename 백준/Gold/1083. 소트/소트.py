N = int(input())
listD = list(map(int,input().split()))
S = int(input())

for i in range(N):
    if S== 0:
        break
    
    max_idx = i
    for j in range(i+1,min(N,i+S+1)):
        if listD[j]>listD[max_idx]:
            max_idx = j

    if max_idx == i:
        continue
    
    moves = max_idx - i
    S-= moves

    for j in range(max_idx,i,-1):
        listD[j],listD[j-1] = listD[j-1],listD[j]
        
print(*listD)