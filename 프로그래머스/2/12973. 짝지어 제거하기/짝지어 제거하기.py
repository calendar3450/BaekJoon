def solution(s):
    answer = -1
    tmp = []
    for i in s:
        if tmp and tmp[-1] == i:
            tmp.pop()
        else:
            tmp.append(i)
    
    if tmp:
        return 0
    else:
        return 1

    return answer