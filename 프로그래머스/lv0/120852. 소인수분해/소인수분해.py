def solution(n):
    divisor = 2
    answer = []
    while True:
        if n % divisor == 0:
            n = n / divisor
            answer.append(divisor)
        else:
            divisor += 1
        
        if n == 1:
            break
    
    return sorted(list(set(answer)))