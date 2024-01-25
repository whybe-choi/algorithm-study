n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)

total = 0
for x, y in zip(a, b):
    total += x*y

print(total)