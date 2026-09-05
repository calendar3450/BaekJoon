def solution(people, limit):
    answer = 0
    people.sort()
    n = len(people)
    arrival = 0
    l = 0
    r = n-1
    
    while l<=r:
        if people[l] +people[r] <= limit:
            l+=1
            
        r-=1
        answer +=1
        
    return answer