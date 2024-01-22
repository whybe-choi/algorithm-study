n, m = map(int, input().split())
s = set()
count = 0

for _ in range(n):
    string1 = input()
    s.add(string1)
    
for _ in range(m):
    string2 = input()
    if string2 in s:
        count += 1
        
print(count)
    