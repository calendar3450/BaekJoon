def solution(n):
    num = 1
    groups = []
    x,y =-1,0
    
    # 2차원으로 채우기
    groups = [[0] * i for i in range(1, n + 1)]
    
    for i in range(n):
        for _ in range(i,n):
            if i%3 == 0:
                x +=1
                
            elif i % 3 ==1:
                y +=1
                
            else:
                x-=1
                y-=1
                
            groups[x][y] = num
            num+=1
            
    answer = []
    for row in groups:
        answer.extend(row)
    return answer