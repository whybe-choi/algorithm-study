def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def solution(n):
    answer = 0
    while factorial(answer) <= n:
        answer += 1
        if factorial(answer) > n:
            answer -= 1
            break
    return answer