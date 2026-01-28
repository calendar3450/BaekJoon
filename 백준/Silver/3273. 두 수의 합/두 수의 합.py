n=int(input())
d=list(map(int,input().split()))
m=int(input())
result=0
d.sort()
for i in d:
    if m-i in d:
        result+=1
print(result//2)