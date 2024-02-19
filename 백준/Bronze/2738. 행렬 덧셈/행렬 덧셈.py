import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

A = []
for _ in range(n):
    elems = list(map(int, sys.stdin.readline().rstrip().split()))
    A.append(elems)
    
B = []
for _ in range(n):
    elems = list(map(int, sys.stdin.readline().rstrip().split()))
    B.append(elems)
    
C = []   
for row in range(n):
    rows = []
    for col in range(m):
        s = A[row][col] + B[row][col]
        rows.append(s)
    C.append(rows)
    
for row in range(n):
    print(*C[row], sep=' ')

     