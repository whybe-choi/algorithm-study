def factorial(n):
    fac = 1
    while n != 0:
        fac *= n
        n -= 1
    return fac

def solution(balls, share):
    answer = factorial(balls) / (factorial(balls - share) * factorial(share))
    return answer