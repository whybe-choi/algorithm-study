def getgcd(num1, num2):
    if num2 > num1:
        num1, num2 = num2, num1
        
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    
    return num1
     

def solution(numer1, denom1, numer2, denom2):
    num1 = numer1*denom2 + numer2*denom1
    num2 = denom1*denom2
    gcd = getgcd(num1, num2)
    
    answer = [num1//gcd, num2//gcd]
    return answer
