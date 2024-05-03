import sys 

n = int(sys.stdin.readline().rstrip())

seq = list(map(int, sys.stdin.readline().rstrip().split()))

# DP 테이블 선언
dp = [-1 for _ in range(n)]

# 초기값
dp[0] = seq[0]

for i in range(n):
    max_sum = 0
    for j in range(n):
        if seq[i] > seq[j]:
            max_sum = max(max_sum, dp[j])
    dp[i] = max_sum + seq[i]

print(max(dp))