def solution(cacheSize, cities):
    answer = 0
    cache = []
        
    if cacheSize == 0:
        answer = len(cities) *5
        
    else:
        for i in range(len(cities)):
            cities[i] = cities[i].lower()
        
        for i in cities:
            if i in cache:
                answer +=1
                cache.pop(cache.index(i))
                cache.append(i)

            elif i not in cache:
                if len(cache)==cacheSize:
                    cache.pop(0)
                    cache.append(i)
                    answer+=5
                else:
                    cache.append(i)
                    answer +=5
                
    return answer