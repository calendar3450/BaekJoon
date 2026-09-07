from collections import Counter

def solution(topping):
    answer = 0
    chul = set()
    bros = Counter(topping)
    
    for t in topping:
        chul.add(t)
        bros[t] -=1
        
        if bros[t] ==0:
            del bros[t]
        
        if len(chul) == len(bros):
            answer +=1
    return answer