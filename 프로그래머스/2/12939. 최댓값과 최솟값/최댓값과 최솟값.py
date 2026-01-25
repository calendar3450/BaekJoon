def solution(s):
    d=list(map(int,str(s).split()))
    d.sort()
    answer=str(d[0])+str(' ')+str(d[-1])
    return answer