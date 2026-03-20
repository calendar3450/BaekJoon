def solution(book_time):
    answer = 0
    hotel = [0]*1500
    
    for book in book_time:
        start_h = int(book[0][0:2])
        start_m = int(book[0][3:])
        start = (start_h * 60) + start_m
        
        finshed_h = int(book[1][0:2])
        finshed_m = int(book[1][3:])
        finsh = (finshed_h*60) + 10 + finshed_m
        
        for i in range(start,finsh):
            hotel[i] +=1
            
    answer = max(hotel)
    
    
    return answer