n,k = map(int,input().split())
s = input()
check = [False] * (n+1)
ans = 0

for i in range(n):
    if s[i] == 'H':
        check[i] = True

for i in range(n):
    if s[i] == 'P':
        if i -k >=0 and i+k <n:
            for j in range(i-k,i+k+1):
                if check[j]:
                    ans +=1
                    check[j] = False
                    break
        elif i-k <0 and i+k <n:
            for j in range(i+k+1):
                if check[j]:
                    ans +=1
                    check[j] = False
                    break
        elif i -k >=0 and i+k >= n :
            for j in range(i-k,n):
                if check[j]:
                    ans +=1
                    check[j] = False
                    break
        elif i-k < 0 and i+k <n:
            for j in range(i+k+1):
                if check[j]:
                    ans +=1
                    check[j] = False
                    break
print(ans)
