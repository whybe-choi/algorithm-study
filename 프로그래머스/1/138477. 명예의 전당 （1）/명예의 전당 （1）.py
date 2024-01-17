def solution(k, score):
    answer = []
    result = []
    for i in score:
        answer.append(i)
        
        if len(answer) > k:
            answer = sorted(answer, reverse=True)[:k]
            
        result.append(min(answer))
    return result