def solution(dirs):
    answer = 0
    n = len(dirs)
    reach = []
    x=0
    y=0
    
    for i in range(n):
        cur = [x,y]
        if dirs[i] == 'L':
            x-=1
            if x<-5:
                x= -5
        elif dirs[i] == 'R':
            x+=1
            if x>5:
                x =5
        elif dirs[i] == 'U':
            y+=1
            if y>5:
                y=5
        else:
            y-=1
            if y<-5:
                y=-5
        
        if [cur,[x,y]] not in reach and cur != [x,y]:
            if [[x,y],cur] not in reach:
                answer+=1
                reach.append([cur,[x,y]])
    return answer