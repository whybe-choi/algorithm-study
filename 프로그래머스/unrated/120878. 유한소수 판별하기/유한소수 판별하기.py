import math

def prime_factors(n):
    factors = []
    i = 2
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n = n / i
        else:
            i = i + 1
    return set(factors)

def solution(a, b):
    gcd = math.gcd(a, b)
    numerator = b // gcd
    factors = prime_factors(numerator)
    
    if factors.issubset({2, 5}):
        answer = 1
    else:
        answer = 2
    
    return answer
