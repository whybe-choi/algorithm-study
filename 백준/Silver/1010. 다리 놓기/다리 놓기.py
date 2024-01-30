import sys

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    result = factorial(m) / (factorial(n) * factorial(m-n))
    print(int(result))