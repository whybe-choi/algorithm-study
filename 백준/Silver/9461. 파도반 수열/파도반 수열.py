import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    
    dp = [0] * 101
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    
    for i in range(4, n+1):
        dp[i] = dp[i-3] + dp[i-2]
        
    print(dp[n])