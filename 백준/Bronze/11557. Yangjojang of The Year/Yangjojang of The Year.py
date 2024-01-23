t = int(input())

for _ in range(t):
    university = dict()
    n = int(input())
    
    for _ in range(n):
        s, l = input().split()
        university[s] = int(l)
        
    print(sorted(university.items(), key = lambda x: x[1])[-1][0])
    