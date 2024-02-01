import sys

a = int(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline().rstrip())
c = int(sys.stdin.readline().rstrip())

prod = str(a * b * c)

for i in range(10):
    print(prod.count(str(i)))
