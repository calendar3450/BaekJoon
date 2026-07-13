def solution(people, limit):
    answer = 0
    l, r = 0,len(people) -1
    people.sort()
    print(people)
    while l<=r:
        if people[l] + people[r] <=limit:
            answer +=1
            l+=1
            r-=1
        elif people[l] + people[r] >limit:
            r-=1
            answer +=1
            
    return answer