def isPrime(n):
    divisor = []
    for i in range(1, n+1):
        if n % i == 0:
            divisor.append(i)  
    if len(divisor) == 2:
        return True
    else:
        return False

def solution(n):
    n_prime = len([i for i in range(1, n+1) if isPrime(i)])
    answer = n - (n_prime + 1) # 1은 소수도 합성수도 아님
    return answer