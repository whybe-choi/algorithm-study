def solution(a, b):
    if a == b:
        answer = a
    else:
        if a > b:
            a, b = b, a
        answer = sum(i for i in range(a, b+1))
        
    return answer