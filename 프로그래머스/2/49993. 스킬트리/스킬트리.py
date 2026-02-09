def solution(skill, skill_trees):
    answer = 0
    skillLeng = len(skill)
    checkingList = []
    
    for skill_tree in skill_trees:
        checking = ''
        
        for ch in skill_tree:
            if ch in skill:
                checking += ch
                
        checkingList.append(checking)
        
    for i in checkingList:
        answerCheck = True
        for ch in i:
            if i.index(ch) != skill.index(ch):
                answerCheck = False
        if answerCheck:
            answer +=1
        
    return answer