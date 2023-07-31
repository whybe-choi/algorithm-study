def solution(array):
    count = {}
    for value in array:
        if value in count.keys():
            count[value] += 1
        else:
            count[value] = 1
            
    maxval = max(count.values()) 
    mode = []
    
    for k, v in count.items():
        if v == maxval:
            mode.append(k)
    if len(mode) > 1:
        answer = -1
    else:
        answer = mode[0]
        
    return answer