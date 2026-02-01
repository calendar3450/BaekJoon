def solution(record):
    answer = []
    log_dict= {}
    logToCheck = []
    
    for log in record:
        tmp = log.split(' ')
        if tmp[0] == 'Enter' or tmp[0] == 'Change':
            log_dict[tmp[1]] = tmp[2]
        
        logToCheck.append([tmp[0],tmp[1]])
        
    for i in range(len(logToCheck)):
        if logToCheck[i][0] == "Enter":
            s = log_dict[logToCheck[i][1]] + '님이 들어왔습니다.'
            answer.append(s)
        elif logToCheck[i][0] == "Leave":
            s = log_dict[logToCheck[i][1]] + '님이 나갔습니다.'
            answer.append(s)
        
    
    return answer