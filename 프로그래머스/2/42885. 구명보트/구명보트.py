def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    l,r = 0,len(people)-1
    
    while l<=r:
        if people[l]+people[r] > limit:
            answer +=1
            l+=1
        else:
            answer +=1
            l+=1
            r-=1
        
    return answer