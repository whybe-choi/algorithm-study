n = int(input())

seq = list(map(int, input().split()))
dp = [0 for _ in range(n)]

# 초기값
dp[0] = 1

for i in range(1, n):
    max_len = 0
    for j in range(i):
        if seq[i] < seq[j]:
            max_len = max(max_len, dp[j])
    
    dp[i] = max_len + 1

print(max(dp))