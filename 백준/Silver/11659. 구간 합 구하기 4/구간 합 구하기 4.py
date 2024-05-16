import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

number = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [0 for _ in range(n)]

for i in range(n):
    if i == 0:
        dp[i] = number[i]
    else:
        dp[i] = dp[i-1] + number[i]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    if i == 1:
        print(dp[j-1])
    else:
        print(dp[j-1]-dp[i-2])