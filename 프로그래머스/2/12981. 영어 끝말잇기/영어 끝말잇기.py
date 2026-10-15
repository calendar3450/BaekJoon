from collections import defaultdict
def solution(n, words):
    answer = []
    lists = []
    len_words = len(words)
    
    lists.append(words[0])
    
    
    for i in range(1,len_words):

        if words[i] in lists or words[i-1][-1] != words[i][0]:
            return [i % n + 1, i // n + 1]
        else:
             lists.append(words[i])   
            
    return [0,0]