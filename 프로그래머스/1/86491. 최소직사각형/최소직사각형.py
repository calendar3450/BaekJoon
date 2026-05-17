def solution(sizes):
    for i in range(len(sizes)):
        if sizes[i][0]>sizes[i][1]:
            sizes[i][0],sizes[i][1]=sizes[i][1],sizes[i][0]
    a=max(sizes)
    a=a[0]
    b=sizes[0][1]
    for j in range(len(sizes)):
        if b<sizes[j][1]:
            b=sizes[j][1]
    total=a*b
    return total