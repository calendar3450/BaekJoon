def solution(begin, target, words):
    answer = 9999999999
    n = len(words)
    wordLeng = len(begin)
    check = [False] * n
    
    if target not in words:
        return 0
    
    def DFS(curWord,cnt):
        nonlocal answer
        
        if curWord == target:
            answer = min(answer,cnt)
            return
        
        # words안의 단어 비교
        for i in range(n):
            diff = 0
            word = words[i]
            
            # words안에 단어중 안바꾼 word인지 확인
            if not check[i]:
                # 단어 비교
                for j in range(wordLeng):
                    if curWord[j] != word[j]:
                        diff +=1
                # 단어 1개 차이면 바꿈.        
                if diff ==1:
                    tmp = curWord
                    curWord = word
                    check[i] = True
                    DFS(curWord,cnt+1)
                    check[i] = False
                    curWord = tmp
    DFS(begin, 0)
        
    return answer