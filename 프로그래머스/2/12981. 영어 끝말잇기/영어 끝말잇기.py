from collections import defaultdict
def solution(n, words):
    answer = []
    lists = []
    len_words = len(words)
    turn = 1
    
    lists.append(words[0])
    
    
    for i in range(1,len_words):
        turn +=1
        if words[i] in lists or words[i-1][-1] != words[i][0]:
            if turn % n == 0:
                return [n,(turn//n)]
            else:
                return [turn%n, (turn//n)+1]
        else:
             lists.append(words[i])   
            
    return [0,0]