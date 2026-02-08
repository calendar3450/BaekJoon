def solution(msg):
    answer = []
    alpha = {'A': 1, 'B':2 , 'C':3, 'D':4 ,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19
            ,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
    lastNum = 27
    curPos = 0
    n = len(msg)
    nextPos = 1
    
    while curPos < n and nextPos <= n:
        if msg[curPos:nextPos+1] not in alpha:
            answer.append(alpha[msg[curPos:nextPos]])
            alpha[msg[curPos:nextPos+1]] = lastNum
            lastNum +=1
            curPos = nextPos
            nextPos = curPos +1
        else:
            nextPos +=1
            if nextPos >= n:
                nextPos = n
                answer.append(alpha[msg[curPos:nextPos]])
                break

    
     
    return answer