import sys 

n = int(sys.stdin.readline().rstrip())

seq = list(map(int, sys.stdin.readline().rstrip().split()))

# DP 테이블 선언
dp = [-1 for _ in range(n)]

# 초기값
dp[0] = 1

for i in range(n):
    max_len = 0
    for j in range(n):
        if seq[i] > seq[j]:
            max_len = max(max_len, dp[j])
    dp[i] = max_len + 1

print(max(dp))