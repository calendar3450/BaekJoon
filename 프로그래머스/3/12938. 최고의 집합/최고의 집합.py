def solution(n, s):
    answer = []
    if n> s:
        return [-1]
    
    divided = s//n
    rest  = s%n
    
    tmp = [divided for _ in range(n)]
    print(tmp)
    
    for i in range(n):
        if rest == 0:
            break
        else:
            tmp[i] +=1
            rest -=1
            
    tmp.sort()
    
    return tmp