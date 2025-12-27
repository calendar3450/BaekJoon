import sys
input = sys.stdin.readline

s = input()
p = [0] *14
k = [0] *14
h = [0] *14
t = [0] *14

total = [13,13,13,13]

lis = [s[i:i+3] for i in range(0,len(s),3)]

for i in lis:
    if i[0] =='P':
        p[int(i[1:3])] +=1
        total[0] -=1
    elif i[0] =='K':
        k[int(i[1:3])] +=1
        total[1] -=1
    elif i[0] =='H':
        h[int(i[1:3])] +=1
        total[2] -=1
    elif i[0] =='T':
        t[int(i[1:3])] +=1
        total[3] -=1

if any(n>=2 for n in p) or any(n>=2 for n in k) or any(n>=2 for n in h) or any(n>=2 for n in t):
    print('GRESKA')
else:
    print(*total)
