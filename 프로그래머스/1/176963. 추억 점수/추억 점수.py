def solution(name, yearning, photo):
    answer = []
    a = dict()
    
    for i, j in zip(name, yearning):
        a[i] = j
        
    for k in photo:
        total = 0
        for x in k:
            if x in a.keys():
                total += a[x]
        answer.append(total)
    return answer