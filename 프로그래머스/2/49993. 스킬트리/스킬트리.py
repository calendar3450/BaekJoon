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
        if i == skill[0:len(i)]:
            answer+=1
        
    return answer