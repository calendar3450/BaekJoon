def solution(fees, records):
    answer = []
    check = {}
    carNumCheck = []
    
    for record in records:
        dList= list(record.split(' '))
        carNumCheck.append(dList[1])
        if dList[2] == 'IN':
            if dList[1] not in check:
                check[dList[1]] = dList[0]
            else:
                 check[dList[1]] = check[dList[1]]+','+dList[0]
        else:
            check[dList[1]] = check[dList[1]] + '-' + dList[0]
    
    carNumCheck = list(set(carNumCheck))
    carNumCheck.sort()

    for carNum in carNumCheck:
        diffs = check[carNum].split(',')
        carDiff= 0
        
        #몇번째 출입인지
        for diff in diffs:
            total = 0
            dif = diff.split('-')
            
            if len(dif) !=2:
                dif.append('23:59')
            
            #출입 마다의 차이
            total1 = 0
            for di in dif:
                d = di.split(':')
                dMinute = int(d[0]) * 60 +int(d[1])
                total1 = dMinute - total1
            #첫 출입 들 합 
            total +=total1
            carDiff += total
            
        if carDiff <=fees[0]:
            answer.append(fees[1])
        else:
            if (carDiff-fees[0])%fees[2]!=0:
                fee = (fees[1]+fees[3]) + ((carDiff-fees[0])//fees[2]) *fees[3]
            else:
                fee = fees[1] + ((carDiff-fees[0])//fees[2]) *fees[3]
                
            answer.append(fee)

    return answer