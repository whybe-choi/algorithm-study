a = set()
b = set()

n, m = map(int, input().split())

for _ in range(n):
    a.add(input())
    
for _ in range(m):
    b.add(input())
    
print(len(a & b))
for i in sorted(list(a & b)):
    print(i)
