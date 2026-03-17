def solution(n):
    answer = []
    group = [[0] * i for i in range(1,n+1)]
    x, y = -1 , 0
    cur_num = 1

    for i in range(n):
        for j in range(i,n):
            if i%3 == 0:
                x+=1
            elif i%3 == 1:
                y+=1
            else:
                x-=1
                y-=1
                
            group[x][y] = cur_num
            cur_num +=1
    
    for i in group:
        answer.extend(i)
        
    return answer
