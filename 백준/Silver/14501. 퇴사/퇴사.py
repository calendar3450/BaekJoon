import sys
input = sys.stdin.readline


N = int(input())
days = []

# 입력받는 곳
for i in range(N):
    a, b = map(int, input().split())
    days.append([a,b])

dp = [0] *(N+1)

for i in range(N-1,-1,-1):
    time = days[i][0]
    pay = days[i][1]

    if i+time <=N:
        dp[i] = max(pay + dp[i+time],dp[i+1])
    else:
        dp[i] = dp[i+1]

print(dp[0])
