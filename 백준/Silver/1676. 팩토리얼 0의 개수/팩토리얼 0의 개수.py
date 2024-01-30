import sys

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

n = int(sys.stdin.readline().rstrip())
fac = str(factorial(n))

count = 0
for num in fac[::-1]:
    if num == "0":
        count += 1
    else:
        break
        
print(count)
