from collections import defaultdict
def solution(genres, plays):
    answer = []
    total = {}
    n = len(plays)
    genres_plays=[]
    
    for i in range(n):
        if genres[i] not in total:
            total[genres[i]] = plays[i]
        else:
            total[genres[i]] +=plays[i]
        
        genres_plays.append([genres[i],plays[i],i])
        
    genres_plays.sort(key=lambda x: (x[0],-x[1]))
    total_sort = sorted(total.items(), key=lambda x: -x[1])
    
    # 여기서 전체 재생횟수
    for i in range(len(total_sort)):
        check = 0
        # 여기서 각각의 재생횟수 확인.
        for j in genres_plays:
            if j[0] == total_sort[i][0] and check <2:
                answer.append(j[2])
                check +=1
        
    return answer