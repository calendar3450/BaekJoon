def solution(s):
    answer = True
    opend= []
    
    for i in s:
        if i == "(":
            opend.append(i)
        else:
            if opend:
                opend.pop()
            else:
                return False
            
    if opend:
        return False
    else:
        return True