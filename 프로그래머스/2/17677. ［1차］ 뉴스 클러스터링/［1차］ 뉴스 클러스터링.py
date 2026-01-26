import math
def solution(str1, str2):
    answer = 0
    n = len(str1)
    m = len(str2)
    str1 = str1.lower()
    str2 = str2.lower()
    union1 = []
    union2 = []
    
    # 각각 집합 구현
    for i in range(n-1):
        sliced = str1[i:i+2]
        check = True
        for j in sliced:
            if not j.isalpha():
                check = False
        if check:
            union1.append(sliced)
        
    for i in range(m-1):
        sliced = str2[i:i+2]
        check = True
        for j in sliced:
            if not j.isalpha():
                check = False
        if check:
            union2.append(sliced)
    
    # 둘다 비었다면 65536 반환
    if not union1 and not union2:
        return 65536
    
    a = union1.copy()
    b = union2.copy()
    # 교집합 만들며 a,b에서 제거
    inter = []
    for x in a[:]:
        if x in b:
            inter.append(x)
            a.remove(x)
            b.remove(x)

    # 합집합 = inter + 남은 a + 남은 b
    allSet = inter + a + b
    
    return math.trunc((len(inter)/len(allSet) * 65536))
    
    
    
    
    return answer