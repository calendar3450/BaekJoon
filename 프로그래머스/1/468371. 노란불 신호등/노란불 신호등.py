def solution(signals):
    answer = 0
    n = len(signals)
    ans = [0] * 3000000
    # 300백만초 안에는 답은 있겠지~
    for i in signals:
        for j in range(3000000//sum(i)):
            for k in range(i[1]):
                ans[sum(i)*j + 1+i[0]+k] += 1
    
    if max(ans) == n:
        return ans.index(max(ans))
    else:
        return -1