def gcd(num1, num2):
    if num2 > num1:
        num1, num2 = num2, num1
        
    while (num2 != 0 ):
        num1, num2 = num2, num1 % num2
    
    return num1

def lcm(num1 ,num2):
    return num1 * num2 / gcd(num1, num2)

def solution(n):
    answer = lcm(n, 6) / 6
    return answer